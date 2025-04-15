# Arithmetic Operators
a = 10
b = 20
print("Arithmetic Operators")
print("a + b = ",a + b)
print("a - b = ",a - b)
print("a * b = ",a * b)
print("a / b = ",a / b)
print("a % b = ",a % b, end ="\n\n")

#Assignment Operators
print("Assignment Operators")
a = 20 #assign 20 to a
print("a is", a)
a += b #Increment the value of a by b's value and then assign to a
print("a  when a += b is ",a)
a -= b #Decrement the value of a by b's value and then assign to a
print("a when a -= b is ",a)
a *= b #Multiply the value of a by b's value and then assign to a
print("a when a *= b is ",a)
a /= b #Divide the value of a by b's value and then assign to a
print("a when a /= b is ",a)
a %= b #Modulo-division of the value of a by b's value and then assign to a
print("a when a %= b is ",a, end = "\n\n")

#Comparison Operators
print("Comparison Operators")
print("a == b", a==b)
print("a < b", a < b)
print("a <= b", a <= b)
print("a > b", a > b)
print("a >= b", a >= b)
print("a != b", a != b, end = "\n\n")

#Logical Operators
print("Logical Operators",end = "\n\n")
print("Truth table of and:")
print("True and True", True and True)
print("True and False", True and False)
print("False and True", False and True)
print("False and False", False and False,end = "\n\n")

print("Truth table of or:")
print("True or True", True or True)
print("True or False", True or False)
print("False or True", False or True)
print("False or False", False or False,end = "\n\n")

print("Truth table of not:")
print("not(True)",not(True))
print("not(False)",not(False))
print("True and True", not(True and True))
print("True and False", not(True and False))
print("False and True", not(False and True))
print("False and False", not(False and False))
print("True or True", not(True or True))
print("True or False", not(True or False))
print("False or True", not(False or True))
print("False or False", not(False or False))