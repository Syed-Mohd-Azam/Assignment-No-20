# Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def function(string):
    lowercase,uppercase=0,0
    for e in string:
        if 65<=ord(e)<=90:
            uppercase=uppercase+1
        elif 97<=ord(e)<=122:
            lowercase=lowercase+1
        else:
            continue
    print("Lowercase letters are :",lowercase)
    print("Uppercase letters are : ",uppercase)
function(input("Enter a string: "))