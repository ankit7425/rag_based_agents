marks = [90,70,60,100,80]
marks.append(85)
marks.extend([75,95])
marks.insert(2,65)
marks.remove(60)
marks.pop(3)


print(marks)
marks.clear()
print(marks)


a=[1,2,2,2,3,3,3,4,4,4,5,5,5,77,8,9,9,9,10]
unique_a = list(set(a))
print(unique_a)



a=[1,2,2,2,3,3,3,4,4,4,5,5,5,77,8,9,9,9,10]
new_list = []
for i in a:
    if i not in new_list:
        new_list.append(i)
print(new_list)



a= [1,2,3,4,5,6,7,8,9,10]
even_sum=0
for i in a:
    if i%2==0:
        even_sum+=i
print(even_sum)
