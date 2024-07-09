# list1= [10,20,30,40]
# list2=["apple","banana","cherry"]
# list3=[10,"apple",20,"banana"]
# list4=list()
#
# print(list1)
# print(list2)
# print(list3)
#
# print(list1[1])
# print(list1[2])
# print(list1[-2])
#
# list5=["apple","banana","cherry","orange","mango","kiwi"]
# print(list5)
# list5[0]="banana"
# print(list5)
#
# print(list5[2:4])
#
# for fruit in list5:
#     print(fruit)
#
# print(len(list5))
# print(list5)
#
# list5.append("cherry")
# print(len(list5))
# print(list5)
#
# list5.insert(4,"grape")
# print(len(list5))
# print(list5)
#
# list5.remove("grape")
# print(list5)
# list5.reverse()
# print(list5)
#
# list5.__delitem__(2)
# print(list5)
# del list5[0]
# print(list5)
#
# list1=list(list5)
# print(list1)
#
# list2=list5.copy()
# print(list2)
#
# print(list1+list2)
#
# for i in list2:
#     list1.append(i)
# print(list1)
#
# print(type(list5))
#
# tupple1=("apple","banana","cherry","orange","mango","kiwi")
#
# print(type(tupple1))
#
pySet={'apple', 'banana', 'cherry', 'orange', 'mango', 'kiwi'}

print(pySet)

for i in pySet:
    print(i)

print("apple" in pySet)

pySet.add("cherry")
print(pySet)
pySet.update(["cherry1"],["cherry2"])
print(pySet)
print(len(pySet))
pySet.remove("cherry2")
print(pySet)
pySet.remove("cherry1")
print(pySet)
pySet.clear()
print(pySet)
print(len(pySet))
del pySet
print(pySet)
