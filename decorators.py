
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f"Took {end - start:.4f} seconds")
        return return_value
    return wrapper


@timer
def is_number(x):
    try:
        float(x)
        return True
    except:
        return False


print(is_number("150"))