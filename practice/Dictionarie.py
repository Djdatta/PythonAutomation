'''
Created on Aug 27, 2020

@author: Dattatray.Jadhav
'''
#A dictionary is a data type similar to arrays


phonebook={}

phonebook["Johns"] =  821678631
phonebook["Dorrels"] = 737253723

print(phonebook)  #{'Johns': 821678631, 'Dorrels': 737253723}

phonebook={
        "John":12344444,
        "Janny": 123343545,
        "janardan" : 943848374
    }

print(phonebook)

for name, number in phonebook.items():
    print("phone number of %s i= %s" %(name, number))
    
    
if "John" in phonebook:
    print("John's contact number is present in phonebook")
else:
    print("Record not present")  
    

   