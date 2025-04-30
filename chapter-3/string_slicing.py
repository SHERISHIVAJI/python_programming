name = input("Enter your name: ")

print("Welcome",name)
print("Length of",name," is:",len(name), end = "\n\n") #length of the string

#access particular index character
print("Access particular index character")
character_at_index_1 = name[1]
print("Character at index 1 is:",character_at_index_1)
print("Character at index 7 is:",name[7])
print("Character at index -4 is:",name[-4])
print("Character at index 5 is:",name[5], end = "\n\n")

#slicing
sliced_name = name[0:5]
print("-----Slicing-----")
print("Sliced name from index 0 to 5 is:", sliced_name)
print("name[ : 5] is", name[ : 5])
print("name[6: ] is", name[6: ], end = "\n\n")

#negative-slicing
print("-----Negative slicing-----")
print("name[-13 : -8]", name[-13: -8])
print("name[ : -8]", name[ : -8])
print("name[-13 : ]", name[-13 : ], end = "\n\n")

#slicing with skip
print("Slicing with skip")
str = "01234567889"
print("str[1:8:2] is :",str[1:8:2])
print("name[0 : 5 : 2] is ", name[0 : 5 : 2])
print("name[ : 9 : 3] is ", name[ : 9 : 3])
print("name[0 : : 2] is ", name[0 : : 2])
print("name[0 : 5 : ] is ", name[0 : 5 : ])
print("name[-13 : 5 : 1] is ", name[-13 : 5 : 1])
print("name[-13 : -8 : 2] is ", name[-13 : -8 : 2])
print("name[-13 : : 2] is ", name[-13 : : 2])
print("name[ :  : 2] is ", name[ : : 2])
print("name[ : -2 : 5] is ", name[0 : -2 : 5])
print("name[-13 :  : 3] is ", name[-13 : : 3])