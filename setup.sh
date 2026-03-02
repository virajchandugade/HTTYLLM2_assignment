#!/bin/bash
chmod +x env_initialization.sh prepare.sh preprocess_dataset.sh

bash env_initialization.sh

bash prepare.sh

echo "Setup complete. The environment is built and folders are ready."