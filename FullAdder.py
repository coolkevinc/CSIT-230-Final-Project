##Created by Kevin Chau
from AND_Gate import AND
from XOR_gate import XOR
from OR_Gate import OR
##using the defined methods of the AND, XOR, and OR Gates from other classes to simulate a Full Adder
def fulladder(a, b):
    AND(a,b)
    XOR(a,b)
a = bool(int(input("Enter 1 or 0: "), 2))
b = bool(int(input("Enter 1 or 0: "), 2))
c = bool(int(input("Enter 1 or 0: "), 2))
print("a = ", int(a), " b = ", int(b), " carry in = ", int(c))
d = XOR(a,b)
e = XOR(d,c)
f = AND(d, c)
g = AND(a, b)
h = OR(f, g)
print("Carry Out:", h)
print("Sum:", e)
