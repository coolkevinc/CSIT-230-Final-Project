##Created by Kevin Chau
##interface class for the NOT gate
def NOT(a): ##defines the NOT Gate
    if(a == True):
        return int(False)
    else:
        return int(True)
def NOTrunner():
    #defines the method that will simulate the NOT Gate
    ##inverts the user input (1 or 0)
    ##run NOTrunner.py for the simulation
    a = bool(int(input("Enter 1 or 0: "), 2))
    if(a == 1):
        x = True
    elif(a == 0):
        x = False
    print("a = ", int(a))
    print("NOT a = ", NOT(a))
