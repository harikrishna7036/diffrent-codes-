import os 
os.system("cls")

x = "Harikrishna"

def greet():
    print("Hi" , x , "Good morning")

print(x)
greet()

def greet():
    global x
    x = "hari"
    print("Hi" , x , "Good evening")


print("hi" ,x )
greet()
print("hi" , x)

# another method 
x = 0 
print(x)
print(type(x))
print("\n")

# string formation either we can give in single quotes or double quotes

name = "harikrishna"
# or 
name = 'harikrishna'
print(type(name))

# string formatting multiple lines through triple quotes 
message = '''Hi

harikrishna

how are you
'''
print(message)


b = "harikrishna is a good boy"
output = b[4:-3]
output1 = b[:-3]
output2 = b[::-1]
print(output2)
print(output1)
print(output)


name = "harikrishna"
print(name.upper())
print(name.lower())
print(name[:4].upper())
print(name[-7:].lower())
print(name.split("a"))




