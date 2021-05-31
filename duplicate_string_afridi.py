str1 = input('Enter a string: ')
global lst
lst = []
def fun(string1):
	if len(string1) > 1:
		if string1[0] == string1[1] :
			return fun(string1[1:])
		else:
			lst.append(string1[0])
			lst.append(string1[1])
			return  fun(string1[1:])
	else:
	    temp = lst[0]
	    lst2 = [temp]
	    for i in lst:
	        if i == temp:
	            continue
	        else:
	            temp = i
	            lst2.append(i)
	    return str(''.join(lst2))

x = fun (str1)
print(x)

	