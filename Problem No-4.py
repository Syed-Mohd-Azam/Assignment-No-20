# Write a python program to create a function that checks whether a passed string is palindrome or not.
def function(string):
    l,s=len(string),""
    i=l-1
    while(i>=0):
        s=string[i]+s
        i=i-1
    if string==s:
        print("String is palindrome!")  
    else:
        print("string is not palindrome")
function(input("Enter a string to check whether a given string is palindrome or not."))