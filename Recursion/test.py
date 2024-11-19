def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1

    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))


# Đệ quy với linked list


class Node :
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    def __str__(self) :
        return str(self.value)
    

Head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

Head.next=A
A.next=B
B.next=C

def reverse_node(node):
    if not node :
        return
    reverse_node(node.next)
    print(node)

reverse_node(Head)