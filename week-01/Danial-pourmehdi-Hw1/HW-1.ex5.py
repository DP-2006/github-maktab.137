from math import factorial

number = 6
factorial = 1
for i in range(1,number+1):
    factorial *= factorial
    print(f" {number}: {factorial}")

number = 6
counter =  1
factorial = 1

while counter <= number:
    factorial *= counter
    counter += 1


print(f"{factorial}")





