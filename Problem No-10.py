# Write a python program to create a function to check whether a string is an anagram or not.
def function(string1,string2):
    l1,l2=[],[]
    for e in string1:
        l1.append(ord(e))
    for e in string2:
        l2.append(ord(e))
    s1,s2=set(l1),set(l2)
    if s1==s2:
        print("Strings are anagram of each other!")
    else:
        print("Strings are not anagram of each other!")
print("Enter the two strings to check whether they are anagram of each other or not!")
function(input("Enter first string: "),input("Enter second string: "))