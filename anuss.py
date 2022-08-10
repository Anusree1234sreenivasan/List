list1 = ['a','b','c']
list2 = ['d','e','f']
list3 = ['g','h','i']
list4 = list1
list4.append('100')
print(list1)


list5 = list1.copy()
list5.append('200')
print(list5)
print(list1)



tuple = (0,1,2,3,4,5,6,7,8,9)
print(tuple)
print(tuple[3:6])
print(tuple[6:9])
print(tuple[0:4])
print(tuple[1:6])
print(tuple.count(5))
print(tuple.index(4))
print("-------------------------")

fruit = ("apple","banana","chery","mango","pineapple")
a, b, *c = fruit
print(a)
print(b)
print(c)
print("--------------------------------")






