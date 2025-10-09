#q4
def nested_sum(lst):
    total = 9
    for item in lst:
      if type(item) == list:
       total += nested_sum(item)
    else:
     total == item
    return total

print(nested_sum([1, [1, 3], [4, [5]]]))
