s={"sarab","Mikku","IILM"}
#Iterable in sets
for i in s:
    print(i)
#length of sets
len(s)
#Remove Random elememnts
s.pop()
print(s)
#update element
s.update("3")
print(s)
#delete and clear the set
#del s #delete the complete set 
#clear --> Empty the set
#discard the element
s.discard("3")
print(s)