#write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|NAME|>,
You are selected!
<|DATE|>'''

name = input('Enter your name: ')
print(letter.replace("<|NAME|>", name).replace("<|DATE|>", "30-April-2025"))