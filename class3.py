import os 
os.system("cls")



# finding the possitive nnumber
a = 2

if a > 0:
    print("possitive")
else:
    print("not possitive")
print("end")        


# to find the remainder
a =  5 
number_10 = (a % 10) == 0
number_5 = (a % 5) == 0 
if number_10:
    print("its devisible by 10")
elif number_5:
    print("number is divisible by 5")
else:
    print("not devisible by 10 or 5") 


# loop condition saticifaction
a = 6 
counter = 0 
while counter < 5:
    a = a+1 
    print(a)
    counter = counter + 1
print("end")


# for statement iterates over each item of sequence
 
word = "Harikrishna"
for each_char in word:
    print(each_char)

# number ranging 
for number in range(1,20):
    print(number)
print("* " * 10)
# random number 
import random 
print(random.randint(1,10))