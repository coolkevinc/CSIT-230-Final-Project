##Created by Kevin Chau
##interface for XOR gate
def XOR(a,b): #defines the XOR Gate
    if(a != b):
        return int(True)
    else:
        return int(False)
def XORrunner():
    ##defines the method that will simulate the XOR Gate
    ##2 user inputs (1 or 0), one output of a XOR b is displayed
    ##run XORrunner.py for the simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    b = bool(int(input("Enter 1 or 0: "), 2))
    if(a != b):
        x = True
    else:
        x = False
    print("a = ", int(a), " b = ", int(b))
    print("a XOR b = ", XOR(a, b))
