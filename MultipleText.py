print('There once was a movie star icon')
print("Who prefered to sleep with light on.")
print("""They learned how to code
a device that sure glowed""")
print("\" and lit up"+' the '+"'NIGHT' \" "+"\nUsing Python!")
#Name is variable / placeholder. 
Name = input("What is your name\n")
print ("Your name is "+Name+".")
print ("Here is diffrence for + & , in Your",Name,".")

#Manipulative with variables.
FirstName = input("Enter Your First name:")
LastName = input("Enter Your Last Name:")
FullName = FirstName + LastName
print("Your Name:",FirstName,LastName)
print(FullName.lower())
print(FullName.upper())
print(FullName.swapcase())
print(FullName.find(LastName))
print(FullName.count('o'))
print(FullName.capitalize())
print("Now your name is ",FullName.replace(LastName,FirstName))