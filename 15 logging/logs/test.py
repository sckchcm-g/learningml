from logger import logging

def add(a, b):
    logging.debug(f'Adding {a} and {b}')
    return a + b

logging.debug('The script has started running')
add(10, 5)