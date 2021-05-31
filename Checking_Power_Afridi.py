#Ridhwan Hossain Afridi

num1 = input('Enter the set of number (number,power): ')

num_list = num1.strip().split(',')
a = float(num_list[0])
b = float(num_list[1])

c = a ** (1.0/b)
count = 0
for i in range(100000):
	if c == i :
		print('True')
		print('{} ** {} = {}'.format(int(c),int(b),int(a)))
		break
	else:
		count += 1
		continue
if count == 100000 :
	print ('False')