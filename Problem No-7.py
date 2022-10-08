# Write a python program to access a function inside a function.
def function(a):
    if a==1:
        return(1)
    else:
        return(a*function(a-1))
print("Factorial of number is : ",function(int(input("Enter a number to find factorial : "))))