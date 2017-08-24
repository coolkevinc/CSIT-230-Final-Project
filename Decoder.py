##Created by Kevin Chau
from AND_Gate import AND
from Not_Gate import NOT
## using the defined methods of the AND and NOT Gates from other classes to simulate an 2-4 Decoder
a = bool(int(input("Enter 1 or 0: "), 2))
b = bool(int(input("Enter 1 or 0: "), 2))
c0 = AND(NOT(a), NOT(b))
c1 = AND(a, NOT(b))
c2 = AND(NOT(a), b)
c3 = AND(a,b)
print("Code:",int(b), int(a))
print("Decoded Code:",c3, c2, c1, c0)
