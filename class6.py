import os 
os.system("cls")

def greet(word):
    msg  = "hello " + word
    return msg

name = "harikrishna"
result = greet(word = name)
print(result)


# a function can have more than one argument
def greet(arg_1,arg_2):
    print(arg_1 + " " + arg_2)

greeting = "hello"
name = "harikrishna"
greet(arg_1=  greeting,arg_2 = name)

# sorting list 
a = (1,2,8,85,6,4)
print(sorted(a))

print(min(a))
print(max(a))
print(sorted(a,reverse=True))