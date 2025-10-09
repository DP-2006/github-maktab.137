#q2 
# def to_string(funk):
#     def warrer(*args, **kwargs):
#         return funk(*args, **kwargs)
#     return warrer
# def print_lenght(funk):
#     def warrer(*args, **kwargs):
#         return funk(*args, **kwargs)
#     return warrer

# @to_string
# @print_lenght

# def exp_funk(a,b,c="Hi"):
#     print(f"{a},{b},{c}")
# exp_funk("Hi", "maktab", "pyhton137")



def to_string(func):
    def wrapper(*args, **kwargs):
        print("to_string")
        str_args = [str(arg) for arg in args]
        str_kwargs = {k: str(v) for k, v in kwargs.items()}
        return func(*str_args, **str_kwargs)
    return wrapper

def print_length(func):
    def wrapper(*args, **kwargs):
        print("print_length")
        for arg in args:
            print(f": {len(str(arg))}")
        return func(*args, **kwargs)
    return wrapper

@to_string
@print_length
def exp_func(a, b, c="Hi"):
    print(f"result: {a}, {b}, {c}")

exp_func("Hi", "maktab", "python137")


        
