# Write a python program to create a function that prints the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
l =[1, 2, 3, 4, 5, 6, 7, 8, 9]
def function(a):
    for e in a:
        if e%2==0:
            print(e,end=" ")
        else:
            continue
function(l)