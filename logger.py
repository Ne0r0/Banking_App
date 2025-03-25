import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_action(action):
    logging.info(action)