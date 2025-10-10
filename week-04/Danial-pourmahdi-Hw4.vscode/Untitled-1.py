#Q.5

def file_io(input_file='input.txt', output_file='output.txt'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(input_file, 'r') as f:
                data = f.read().strip()
                  result = func(data, *args, **kwargs)
                  with open(output_file, 'w+') as f:
                f.write(str(result))
            return result
        return wrapper
    return decorator
@file_io(input_file='input.txt', output_file='output.txt')
def process_data(data):
    return data.upper()
        return data.upper()

    process_data()

