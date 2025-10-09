#q2 
def to_string(funk):
    def warrer(*args, **kwargs):
        return funk(*args, **kwargs)
    return warrer
def print_lenght(funk):
    def warrer(*args, **kwargs):
        return funk(*args, **kwargs)
    return warrer

@to_string
@print_lenght

def exp_funk(a,b,c="Hi"):
    print(f"{a},{b},{c}")
exp_funk("Hi", "maktab", "pyhton137")




        
