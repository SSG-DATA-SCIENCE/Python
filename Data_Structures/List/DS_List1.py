# List []
list=[1,2,3,4,"Sarab",8,7.9]
print(list)
#lenght of List
print(len(list))
#accessing the items from list
print(list[1])
print(list[-4])
#accessing the items from list between two indexes
print(list[4:7])
#adding new item
list.append("Orange")
print(list)
#adding new item at particular position
list.insert(2,"Cherry")
print(list)
#append element from another iterable
my_list=["Apple","Banana","Cherry"]
list2=["Potato","tomato"]
my_list.extend(list2)
print(my_list)
#repetation operation in list
print([0]*10)
print([1,2]*5)
#membership in ,not in
print("Apple" in my_list)
print("Check" not in my_list)