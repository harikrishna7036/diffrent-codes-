import os 
os.system("cls")

num = input("Enter Number >")

if num.isdigit():
    print(int(num) + 10)
else:
    print("this is not a number \n please try again")


eassy = "my name is harikrishna iam from hyderabad"
print("-".join(eassy))

print("a".count(eassy))


phno = "9381656917"
name = phno[-2:]
print(name.zfill(10))

word= input("Enter Number >")
length = len(word)
masking = length - 2 
print(word[0] + "*" * masking + word[length - 2])


name = "python is high level programming laungage"
print("a" in name)
print("is" not in name)


# string concatenation is only possible with the strings 
name = input("Enter Nmae >")
print("Hi " + name.upper() + " Happy new year")

name = "harikrishna"
result = f" Hi  {name.upper()} Happy new year"
print(result)