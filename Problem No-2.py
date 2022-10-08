# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def function(a):
    for e in range(2,a,1):
        if a%e==0:
            print(a," is not prime number! ")
            break
        else:
            continue
    else:
        print(a," is a prime number!")
function(int(input("Enter a number to check whether it is prime or not: ")))