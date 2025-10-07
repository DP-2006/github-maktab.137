#q.7
def add_numbers(a,b,/):
    return a + b 
def print_info(*,name,age):
     print(f"Name: {name}, Age: {age}")
def calculator(a, b, /, *, operator):
 if operator == '+':
  return a + b
 elif operator == '-':
  return a - b
 elif operator == '*':
  return a * b
 elif operator == '/':
  return a / b
 else:
  return "faill opration "
 

print(add_numbers(5,3))
print(calculator(10, 5, operator='+'))
print(calculator(11, 5, operator='-'))
print(calculator(12,4,operator='*'))
print(calculator(9,3,operator='/')) 