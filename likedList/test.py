class SinglyNode:
    def __init__(self,value,next=None) :
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)
    

Head = SinglyNode(1)


A = SinglyNode(2)
B = SinglyNode(4)
C = SinglyNode(9)

Head.next=A
A.next=B
B.next=C


cur = Head

while cur :
    print(cur)
    cur=cur.next


def countNode (Node) :
    count = 0
    cur = Node
    while cur :
        count += 1
        cur = cur.next
    return count

def display (Head):
    elements =[]
    cur = Head
    while cur:
        elements.append(str(cur.value))
        cur=cur.next
    return f"{'->'.join(elements)}"
print('count node',countNode(Head))
print('list node',display(Head))

def search(Head,value):
    cur=Head
    while cur:
        if cur.value == value:
            return True
        cur=cur.next
    return  False

print(search(Head,4)) 
    