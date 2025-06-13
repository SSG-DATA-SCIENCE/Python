#comprehension
prices=[10,20,4,60]
double_price=[price*2 for price in prices]
print(double_price)
#Condtional list Comprehension
a=[1,2,3,4,5]
result=[n for n in a if n%2==0]
print(result)
#Nested list Comprehension
pairs=[[x,y] for x in [1,2,3] for y in [4,5,6]]
print(pairs)
