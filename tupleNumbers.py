#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with 
#those numbers.

numbers = input("Enter the numbers: ")
lst = numbers.split(",")
tup = tuple(lst)
tup