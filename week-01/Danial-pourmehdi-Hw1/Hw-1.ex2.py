
n = input("enter the number ")
u=0

if n.isdigit():
    n = int(n)
    if n <= 1:
        print("NO")
    else:
        total = 0
        for i in range(2, n):
            u = n / i
            if n % i == 0:
               total += u
               print(f"{total}:{i}")
        if total+1 == n :
            print("true")
        else:
            print("Flse")
else:
    print("NO - invalid number")
