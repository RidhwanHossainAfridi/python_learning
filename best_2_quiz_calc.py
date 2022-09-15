% Marks Percentage Quiz Best 2
x = input('Enter')
x = x.split(',')
lst = list()
for i in x:
    m = float(i)
    x = lst.append(m)
lst.sort(reverse = True)
avg = (lst[0]+lst[1])/2
per = avg*100/20
print(lst)
print(avg)
