'''
Created on Aug 27, 2020

@author: Dattatray.Jadhav
'''

class Test:
    
    var1="Tiger"
    def function1(self):
        print("This is the first function")
        var2="Lion"

testObject=Test()
testObject.function1()
print("Given args is : %s" %(testObject.var1))

obj2=Test()
obj2.var1="lion"
print(obj2.var1)