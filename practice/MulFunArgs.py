'''
Created on Aug 28, 2020

@author: Dattatray.Jadhav
'''
class Test:
    def foo(self,first, second, third, *therest):
        print("First: %s" % first)
        print("Second: %s" % second)
        print("Third: %s" % third)
        print("And all the rest... %s" % list(therest))
        
test=Test()
test.foo(1, 2, 3,4,5,6,7,8)

'''OUTPUT
First: 1
Second: 2
Third: 3
And all the rest... [4, 5, 6, 7, 8]
'''
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
