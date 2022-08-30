class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
def kth_to_last_node(k, head):
    
    if k == 0:
        raise Exception("k == 0")
    ptr1 = head
    ptr2 = head
    listLen = 1
    
    while ptr1.next:
        ptr1 = ptr1.next
        listLen += 1
    
    if k > listLen:
        raise Exception("k > size of the list")
    
    while listLen > k:
        ptr2 = ptr2.next
        listLen -= 1
       
    return ptr2

print(kth_to_last_node(0,a).value)