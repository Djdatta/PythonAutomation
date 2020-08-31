'''
Created on Aug 26, 2020

@author: Dattatray.Jadhav
'''

print("Simple function")
def demo():
    print("This is the first function code")

demo()

print("Parameterizes function")

def parametrsFunc(username, greeting):
    print("Hello %s, Wish you %s" %(username,greeting))
    
parametrsFunc("Dattatrat", "Happ Birthday")

def add(a,b):
    print("Addition = %d" %(a+b))
    print("Subtraction = %d" %(a-b))
    print("Multiplication = %d" %(a*b))
    print("Division = %d" %(a/b))
    print("reminder = %d" %(a%b))
    
add(12, 2)