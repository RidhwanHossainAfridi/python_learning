# assignment Marks Percentage calculator
x = input('Enter')
x = x.split(',')
lst = list()
for i in x:
    m = float(i)
    x = lst.append(m)
avg = (sum(lst)/(100+120+120+140))*100
num2 = (10*avg)/100
print(lst)
print(num2)
