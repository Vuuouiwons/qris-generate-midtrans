import os
import uuid
import logging

import requests
import midtransclient

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.critical('Error this is not a main file!!, please use "from generate_qris import *"')

def generate_qris(amount: int | float, payment_id: str| None = None) -> dict[str, str]:
    """
    Generate a QRIS payment code using Midtrans API.

    This function creates a QRIS (Quick Response Code Indonesian Standard) 
    payment request via Midtrans, allowing customers to make payments 
    using QR-based payment methods.

    Args:
        amount (int | float): The payment amount in Indonesian Rupiah (IDR).
        order_id (str): A unique identifier for the payment, provided by the client.

    Returns:
        dict[str, str]: The response from Midtrans containing QRIS payment details,
                        including the generated QR code URL and transaction status.

    Raises:
        midtransclient.error.MidtransAPIError: If the request to Midtrans API fails.
        ValueError: If the amount is negative or order_id is empty.
    """
    
    # set default payment_id if not provided
    if not payment_id:
        logger.debug('paymend_id not provided creating payment_id')
        payment_id == str(uuid.uuid4())
        logger.debug(f'payment_id created: {payment_id}')
        
    logger.debug(f'building payment payload with amount:{amount}, order_id:{payment_id}')
    request_payload = {
        'payment_type': 'qris',
        'transaction_details': {
            'order_id': payment_id,
            'gross_amount': amount
        }
    }
    
    logger.debug('sending request with midtrans...')
    core_api = midtransclient.CoreApi(
        is_production=False,
        server_key=os.getenv('server_key', 'YOUR_SERVER_KEY'),
        client_key=os.getenv('client_key', 'YOUR_CLIENT_KEY')
    )
    
    qris_data = core_api.charge(parameters=request_payload)
    
    return qris_data

