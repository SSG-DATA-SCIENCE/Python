#shallow copy 
lis=["Apple","Orange","Cherry"]
a=lis
lis[0]="Banana"
print(lis)
print(a)
#deep copy
import copy
a=[[1,2,3],[4,5,6]]
b=copy.deepcopy(a)
b[0][0]=100
print(b)
print(a)
#pop
lis.pop()
print(lis)
#delete
del lis
print(lis)