num = input("Enter a number: ")
lst = []
lst2 =[]
for i in num:
	i = int(i)
	lst.append(i)
x = sum(lst)

while x > 10 or x < 0:
	x = str(x)
	for j in x:
		j = int(j)
		lst2.append(j)
	x = sum(lst2)
print(x)
		
	