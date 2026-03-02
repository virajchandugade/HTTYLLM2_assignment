import os
import datasets as ds

# "./test_output/preprocessed_{rank}.txt....(used this link for testing locally, and below logic to create a output directory)"
# output_dir = os.path.dirname(OUTPUT_FILE_TEMPLATE)
# if output_dir and not os.path.exists(output_dir):
#     print(f"Creating directory: {output_dir}")
#     os.makedirs(output_dir, exist_ok=True)

OUTPUT_FILE_TEMPLATE ="/shared-file-storage/preprocessed_data/preprocessed_{rank}.txt"


def preprocess_text(text):
    return text.lower().strip().split()

def load_dataset(r, total_proc):
  
    #streaming=true, ensures that we are streaming and not dowloading 10tb of data
    #shard method helps parallel processing, by giving unique slices for all processes
    dataset=ds.load_dataset("allenai/c4", "en",split="train", streaming=True)
    print(dataset.shard(num_shards=total_proc,index=r))
    return dataset.shard(num_shards=total_proc,index=r)
    
'''write_[reprocessed_text: this function processes ands writes data row by row
by performing preprocess_text here inside the loop and writing the file immediately.
This ensures the previous tokens to be erased in ram for each iteration(2gb ram constraint) '''   
def write_preprocessed_text(preprocessed_text, rank):
    with open(OUTPUT_FILE_TEMPLATE.format(rank=rank), "w") as f: #encoding="utf-8" to test locally
        for line in preprocessed_text:
            tokens=preprocess_text(line['text'])
            f.write("\t".join(tokens))
            f.write("\n")

def main():
    local_rank = int(os.environ.get("PROC_RANK",0)) 
    total_procs = int(os.environ.get("TOTAL_PROCS",1)) 
    text_to_process = load_dataset(local_rank,total_procs) 
    
    write_preprocessed_text(text_to_process, rank=local_rank)

if __name__ == "__main__":
    main()