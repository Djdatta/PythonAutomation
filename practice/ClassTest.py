'''
Created on Jan 29, 2020

@author: Dattatray.Jadhav
'''

class MyClass:
    '''
    classdocs
    '''


    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)
    

c1 = MyClass("datta",28)
print(c1.name)
print(c1.age)
c1.age=32   # Set value
print(c1.age)
#del c1.age     --delete age
#del c1        -- delete object
c1.myfunc()

c2 = MyClass("Rahul", 29)

print("Name = ",c2.name, "age = ",+c2.age)  # + is optional but , is commpulsory


class Test(MyClass):        #child class
    
    print("Hello This is new class")
    x=MyClass("Raj",21)
    x.myfunc()
    