#String functions in python are used to perform operations or manipulate string

s = input("Enter your string: ")

print("len(s) function returns:", len(s), end = "\n\n")

# Case and Formatting Methods
print("-----Case and Formatting Methods-----")
print("s.lower()->", s.lower()) #Converts to lowercase
print("s.upper()->",s.upper()) #Converts to uppercase
print("s.title()->", s.title()) #Capitalizes each word
print("s.capitalize()->", s.capitalize()) #Capitalizes first letter
print("s.swapcase()->", s.swapcase()) #Swaps case
print("s.casefold->", s.casefold(), end="\n\n") #Aggressive lowercase for comparison

# Searching and Counting
print("-----Searching and Counting-----")
print("s.find(\"Python\")->", s.find("Python")) #Returns index of first match or -1
print("s.find(\"python\")->", s.find("python")) #Returns index of first match or -1
print("s.index(\"Python\")->", s.index("Python")) #Like find() but raises error if not found
print("s.rfind(\"o\")-.", s.rfind("o")) #Last occurrence of substring
print("s.rindex(\"o\")->", s.rindex("o")) #Last index (error if not found)
print("s.count(\"o\")->", s.count("o")) #Counts occurrences
print("s.count(\"O\")->", s.count("O")) #Counts occurrences
print("s.startswith(\"He\")->",s.startswith("He")) #Checks start of string
print("s.startswith(\"Hi\")->",s.startswith("Hi")) #Checks start of string
print("s.endswith(\"! \")->",s.endswith("! ")) #Checks end of string
print("s.endswith(\"!\")->",s.endswith("!"), end = "\n\n") #Checks end of string
# print("s.index(\"python\")->", s.index("python")) #Like find() but raises error if not found
# print("s.rfind(\"O\")-.", s.rfind("O")) #Last occurrence of substring
# print("s.rindex(\"O\")->", s.rindex("O")) #Last index (error if not found)

# Trimming and Padding
print("-----Trimming and Padding-----")
print("s.strip()->", s.strip()) #Removes whitespace from both ends
print("s.lstrip()->", s.lstrip()) # Removes left spaces	
print("s.rstrip()->", s.rstrip()) #Removes right spaces	
print("s.zfill(25)->", s.zfill(25)) #Pads with zeros
print("s.rjust(30)->", s.rjust(30)) #Right justify with spaces
print("s.ljust(25)->", s.ljust(25)) #Left justify with spaces	
print("s.center(50)->", s.center(50)) #Center with padding	
