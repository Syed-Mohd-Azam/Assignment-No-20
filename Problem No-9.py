# Write a python program to create a function to check whether a string is a pangram or not.
def function (string):
    l1=list(range(97,123,1))
    s1=set(l1)
    l=[]
    for e in string :
        if 97<=ord(e)<=122 :
            l.append(ord(e))
        elif 65<=ord(e)<=90:
            l.append(ord(e)+22)
        else:
            continue
    s2=set(l)
    if s1==s2:
        print("Given string is Pangram !")
    else:
        print("Given string is not pangram!")
function(input("Enter a string: "))