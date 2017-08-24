##Created by Kevin Chau
##interface class for the NAND gate
def NAND(a,b): ##Define the NAND Gate
    if(a == True and b == True):
        return int(False)
    else:
        return int(True)
def NANDrunner():
    ##Defines the method that will simulate the NAND Gate
    ##2 user inputs (1 or 0), one output of a NAND b
    ##run NANDrunner.py for simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    b = bool(int(input("Enter 1 or 0: "), 2))
    if (a == 1 or b == 1):
        x = False
    else:
        x = True
    print("a = ", int(a), " b = ", int(b))
    print("a NAND b = ", NAND(a, b))
