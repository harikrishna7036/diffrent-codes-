import os 
os.system("cls")



# break statement
for i in range(10):
    if i == 5:
        break 
    print(i)
print("end")

# continue satatement 
for i in range(10):
    if  i == 6:
        continue 
    print(i)
print("end")

# pass satatement is used as syntatctic place holder when it is excecuted nothing will happen


# to find the unicode value  and charecter values
for i in range(62,91):
    print(chr(i))

print(ord("j"))

print("A" < "b")

# rounding numbers 

a = 3.1455 
print(round(a,1))

print(round(a))


# to find integral part of the quotient we  use floor division operator
a = 10 
b = 2 
c = a//b 
print(c)

# compound assignment operator 
a = 10 
a += 2 
print(a)
# to find the id of the object
a = [1,2,3,"six"]
print(id(a))

# split a string into a list at every specified separator 
nums = "1 2 3 4"
print(nums.split())