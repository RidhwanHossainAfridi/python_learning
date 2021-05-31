
#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name:  "))

revfname = fname[::-1] #this is the fastest way to reverse a string
revlname = lname[::-1]

print("The reverse of your name is: " + revfname + " " + revlname)