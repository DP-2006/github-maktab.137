#Q.3

def most_repetly(list):
    return max(set(list),key= list.count)
most_repetly
my_list = [1,2,3,4,5,66,6,6,7,7,8,8,8,9,10]
result = most_repetly(my_list)
print result

