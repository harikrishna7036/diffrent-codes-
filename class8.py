
import os 
os.system("cls")




def get_largest_sqr(list_x):
    length = len(list_x)
    for i in range(length):
        x = list_x[i]
        list_x[i] = x * x 
        largest = max(list_x)
        return largest 


list_a = [1 ,-3,4,-8]
result = get_largest_sqr(list_a)
print(result)
