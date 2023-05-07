



#--------------------------------
#----- User input------
#--------------------------------




# input("Hello Python") # Hello Python

fName = input("What is Yout First Name :") # What is Yout First Name :salar
mName = input("What is Yout Middle Name :") # What is Yout Middle Name : Issa
lName = input("What is Yout Last Name :") # What is Yout Last Name : Issa

fName = fName.strip().capitalize() # Hello Salar Issa Issa Nice to Meet you
mName = mName.strip().capitalize() ## Hello Salar Issa Issa Nice to Meet you
lName = lName.strip().capitalize() # Hello Salar Issa Issa Nice to Meet you

print(f"Hello {fName} {mName} {lName} Nice to Meet you") # Hello salar issa issa Nice to Meet you
print(f"Hello {fName.strip().capitalize()} {mName.strip().capitalize():.1s} {lName.strip().capitalize()} Nice to Meet you") # Hello Salar I Isa Nice to Meet you




