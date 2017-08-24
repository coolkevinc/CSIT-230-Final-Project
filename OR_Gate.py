##Created by Kevin Chau
##interface for XOR gate
def OR(a,b): ##defines the OR Gate
    if(a == False and b == False):
        return int(False)
    else:
        return int(True)
def ORrunner():
    ##defines the method that will simulate the OR Gate
    ##2 user inputs (1 or 0), the output of a OR b is displayed
    ##run ORrunner.py for the simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    b = bool(int(input("Enter 1 or 0: "), 2))
    if(a == 1 or b == 1):
        x = True
    elif(a != b):
        x = True
    else:
        x = False
    print("a = ", int(a), " b = ", int(b))
    print("a OR b = ", OR(a, b))
