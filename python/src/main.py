import os
import logging
import uuid
from modules.payment import generate_qris

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logger.info(f'Running {__name__}')
    
    print(generate_qris(amount=10000, order_id=str(uuid.uuid4())))