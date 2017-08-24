##Created by Kevin Chau
##interface for XNOR gate
def XNOR(a,b): ##defines the XNOR Gate
    if(a == False and b == False):
        return int(True)
    elif(a == True and b == True):
        return int(True)
    else:
        return int(False)
def XNORrunner():
    ##defiines the method that will run the XNOR Gate
    ##2 user inputs (1 or 0), one output of a XNOR b is displayed
    ##run XNORrunner.py for the simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    b = bool(int(input("Enter 1 or 0: "), 2))
    if (a == b):
        x = True
    else:
        x = False
    print("a = ", int(a), " b = ", int(b))
    print("a XNOR b = ", XNOR(a, b))
