import os 
os.system("cls")

# extended slicing nad string method
name = "harikrishna"
result = name[0:11:2]
print(result)

# python has set of built in reusabilities 
name = "    harikrishna ..,,"
result = name.strip(" .,")
print(result)


# to find isdigit
print(name.isdigit())

# to replace 
print(result.replace("hari" , "vamshi"))

#nested condition loop an innner loop within the repeating block of an outer looop is called nested loop condition


for i in range(3):
    print("outer :" + str(i))
    for j in range(3):
        print("inner :" + str(j))