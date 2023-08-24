import logging

def log_function_call(func):
    def decorated(*arg, **kwarg):
        logging.info(f"Calling {func.__name__} with args = {arg}, kwarg = {kwarg}")
        result = func(*arg, **kwarg)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a,b):
    return a+b

my_function(4,5)