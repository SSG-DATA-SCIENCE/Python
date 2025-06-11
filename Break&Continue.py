#1st Break Statement
print("Break output")
b=[1,2,7,"Sarab","AjaySir"]
for i in b:
    print(i)
    if i==7:
     break
#2nd Continue Statment
print("Continue Output")
n=7
c=1
while c<n:
    c=c+1
    if c==5 or c==6:
        continue
    print(c)