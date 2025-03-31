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

## Running the code
Before running the script, update run_example.sh with your credentials. Then, execute the following command:

```bash
cd src
bash run_example.sh
```

This will initiate the QRIS payment process with the configured parameters.
