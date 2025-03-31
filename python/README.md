# Python QRIS Payment Gateway
## File Structure
```
.
├── README.md
├── requirements.txt
└── src
    ├── main.py
    ├── modules
    │   └── payment.py
    └── run_example.sh
```
## Overview
This project provides a QRIS payment gateway in Python. The core function for generating a QRIS code is located in `./src/modules/payment.py`.

## Setup
This project uses Conda as a virtual environment manager. Before running the code, make sure you have [conda installed](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). 
After conda is installed, you can run `$ bash env_setup.sh` to assist the virtual environment creation and depedencies installation.

## Running the code
Before running the script, update run_example.sh with your credentials. Then, execute the following command:

```bash
cd src
bash run_example.sh
```

This will initiate the QRIS payment process with the configured parameters.
