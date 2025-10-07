pr = input().lower()
pr = pr.replace(" ", "")
for x in "aueio":
    pr = pr.replace(x, ".")
pr = pr[::-1]
print(pr)
