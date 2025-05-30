import logging

## logging settings


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('airthmeticApp.log'),
        logging.StreamHandler()
    ]
)


logger=logging.getLogger("AirthmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b} = {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {b} from {a} = {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} by {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero error when dividing {a} by {b}")
        return None

add(10, 15)
subtract(1, 5)
multiply(32, 7)
divide(10, 0)