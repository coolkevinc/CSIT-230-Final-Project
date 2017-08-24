##Created by Kevin Chau
from OR_Gate import OR
from Not_Gate import NOT
from AND_Gate import AND
##using the defined methods of the OR, NOT, and AND Gates from other classes to simulate an 4-2 encoder
a0 = bool(int(input("Enter 1 or 0: "),2))
a1 = bool(int(input("Enter 1 or 0: "),2))
a2 = bool(int(input("Enter 1 or 0: "),2))
a3 = bool(int(input("Enter 1 or 0: "),2))
f0 = OR(a1, a3)
f1 = AND(NOT(a1), NOT(a0))
print("Code:",int(a3), int(a2), int(a1), int(a0))
print("Encoded Code:",f1, f0)
