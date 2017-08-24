##Created by Kevin Chau
##interface class for the NOR gate
def NOR(a,b): ##defines the NOR Gate
    if(a == False and b == False):
        return int(True)
    else:
        return int(False)
def NORrunner():
    ## defines the method to simulate the NOR Gate
    ##2 user inputs (1 or 0), one output of a NOR b
    ##run NORrunner.py for the simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    b = bool(int(input("Enter 1 or 0: "), 2))
    if(a == 0 or b == 0):
        x = True
    else:
        x = False
    print("a = ", int(a), " b = ", int(b))
    print("a NOR b = ", NOR (a, b))
