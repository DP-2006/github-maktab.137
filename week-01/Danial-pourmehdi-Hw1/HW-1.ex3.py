try:
    temperature = float(input("enter temperature: "))
    if temperature < 10:
        print("cold water")
    elif 10 <= temperature <= 25:
        print("normal water")
    else:
        print("Hot water")

except ValueError:
    print(" enter a number ")