import os 
os.system("cls")

class mobile:
    def __init__(self,model,camera):
        self.model = model 
        self.camera = camera 
    def make_cal(self,number):
        print("calling....")

mobile_obj = mobile("iphone 6 pro" , "64mp")
print(mobile_obj)
print(id(mobile_obj))
print(mobile_obj.model)
print(mobile_obj.mobile)