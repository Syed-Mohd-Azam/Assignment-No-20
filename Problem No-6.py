# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def function():
    l=[]
    for e in range(2,30,1):
        l.append(e*e)
    print(l)
function()