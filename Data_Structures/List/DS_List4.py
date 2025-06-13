#list as stack
stack=[]
stack.append("1")
stack.append("2")
stack.append("3")
stack.append("4")
print(stack)
stack.pop()
print(stack)
#list as queue
from collections import deque
queue=deque()
queue.append("A")
queue.append("B")
queue.append("C")
queue.append("D")
print(queue)
while queue:
    alphabet=queue.popleft()
    print("Alphabet", alphabet)