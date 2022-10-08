# Write a python program to create a function to find the Min of three numbers.
def function(x,y,z):
    l=[x,y,z]
    return(min(l))
print("Enter three values to find minimum : ")
a,b,c=int(input("Enter first number : ")),int(input("Enter second number: ")),int(input("Enter third number: "))
print("Minimum value is : ",function(a,b,c))