#q2 
def to_string(func):
    def wrapper(*args, **kwargs):
        str_args = [str(args) for arg in args]        
        str_kwargs = {K: str(v) for k, v in kwargs.items()}
        return func
    return wrapper

def print_lenght(func):
    def wrapper(*args,**kwargs):
        for arg in args:
            print(f"lenght for arg: {len(arg)}")
        for k, in kwargs.items:
            print("lenght for arg v")
        return func
    return wrapper

@to_string
@print_lenght
def exp_func(a, b, c="Hi"):
    print(f" a:{a}, b:{b}, c:{c}, d:{d}")




        