# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def function(l):
     return(list({e for e in l}))
l=["Python","Django","Reactjs",2,3,3,2,"Python","Django","iNeuron","iNeuron","Django",2,3,2]
print("List having unique elements:" ,function(l))