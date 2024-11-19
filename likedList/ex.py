class Node :
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.value)

def insert_at_beginning(head,data):
        new_note = Node(data)
        if head :
            new_note.next=head
            head.prev = new_note
        
       
        return new_note
def display(head):
        cur = head
        element = []
        while cur :
            element.append(str(cur.value))
            cur=cur.next
        print("<->".join(element))




head = Node(2)
head = insert_at_beginning(head,10)
head = insert_at_beginning(head,20)
print(head.next.prev)
display(head)

# w

# none <-> 10 <-> none
# none <-> 9 <-> 10 <-> none

print(298%11)