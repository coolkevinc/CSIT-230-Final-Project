##Created by Kevin Chau
##Defining the function of an AND gate
def AND(a,b):
    if(a == True and b == True):
        return int(True)
    else:
        return int(False)
##2 user inputs (1 or 0), one output of a*b is displayed
a = bool(int(input("Enter 1 or 0: "), 2))
b = bool(int(input("Enter 1 or 0: "), 2))
if(a == 1 or b == 1):
    x = True
elif(a == 0 or b == 0):
    y = False
print("a = ", int(a), " b = ", int(b))
print("a*b = ", AND(a, b))
