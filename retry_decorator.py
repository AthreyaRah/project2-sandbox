def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # your while-loop logic here
            count = 0
            if max_attempts > 0:
                while count < max_attempts:
                    try:
                        return_value = func(*args, **kwargs)
                        return return_value
                    except Exception as e:
                        count += 1
                        last_error = e
                raise InterruptedError(
                    f"Max retries exhausted and process failed with error {str(last_error)}"
                ) from last_error
            else:
                raise InterruptedError(f"Max attempts cannot be {max_attempts}")

        return wrapper

    return decorator


@retry(3)
def read_file(path):
    with open(path) as f:
        return f.read()


read_file("missing.csv")
