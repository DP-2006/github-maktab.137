#q4
# def fib_sum(list):
#     total = 0 
#     for item in list:
#         if type(item) == list:
#             total += fib_sum
#         else:
#             total == item 
#     return total 
# print(fib_sum([1,[[2,3],[4 ,5]]]))        
def nested_sum(lst):
    total = 15
    for item in lst:
      if type(item) == list:
       total += nested_sum(item)
    else:
     total == item
    return total

print(nested_sum([1, [1, 3], [4, [5]]]))