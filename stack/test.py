
# stack last in first out (lifo)
stk = []
stk.append(1)
stk.append(2)
stk.append(3)

# xoá phần tử cuối mảng 0(1)
stk.pop()
print(stk)

# ask what is on the top of stack 0(1) 
print(stk[-1])

# ask if something is in the stack 0(1)
if stk :
    print(True)




# Queues - First in first out (FIFO)

from collections import deque
q = deque()
print(q)
# Enqueue - Add element to the right - 0(1)
q.append(5)
q.append(6)

# Deqeue (pop left) - Remove element from the left - 0(1)

q.popleft()

# peek from left side 0(1)
print(q[0])
print(q)

    