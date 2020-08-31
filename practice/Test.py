'''
Created on Aug 25, 2020

@author: Dattatray.Jadhav
'''
from textwrap import indent

print("Hello")

mylist = [1,22,3]
print(mylist[1])


number = 1*2+1-1/2-2
print(number)

reminder=11%3
print("reminder is %d") # When we want to print int use %d


div=13/3
print(div)

print([1,2,3] * 3 )  # output:[1, 2, 3, 1, 2, 3, 1, 2, 3]

name = "John"
age = 23

print("%s is %d years old." % (name, age))
print("His name is: "+name) # for string we use %s or +var

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

'''

string = "my name is Datta"

print("length of string =%d" %len(string))

print("first occurrence of n is =%d " % string.index("n"))

print("a occurs %d times " % string.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % string[:5]) # Start to 5
print("The next five characters are '%s'" % string[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % string[12]) # Just number 12
print("The characters with odd index are '%s'" %string[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % string[-5:]) # 5th-from-last to end

print("uppr case is %s" % string.upper())
print("lower case is %s" % string.lower())

s=string[-5:]

print("given string is in upper case : %s " %s.isupper())


#While loop

print("While loop")
count=0
while count <5:
    print(count)
    count+=1
  
print("for loop--to print odd number")    
for x in range(10):
    if x % 2==0:
        continue        # continue is used to skip the current block. so it will print odd number
    print(x)    
    
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")