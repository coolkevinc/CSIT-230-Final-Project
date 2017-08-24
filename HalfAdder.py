##Created by Kevin Chau
from AND_Gate import AND
from XOR_gate import XOR
##using the defined methods of the AND and XOR Gates from other classes to simulate a half-adder
def halfadder(a, b):
    AND(a,b)
    XOR(a,b)
a = bool(int(input("Enter 1 or 0: "), 2))
b = bool(int(input("Enter 1 or 0: "), 2))
print("a = ", int(a), " b = ", int(b))
print("Carry:", AND(a, b))
print("Sum:", XOR(a, b))
