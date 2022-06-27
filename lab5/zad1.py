text=input("napisz wyraz: ")
space=0
letters=0
for char in text:
    char = char.lower()
    if char  == ' ':
        space+=1
    else:
        letters+=1
print("spacja:", space)