# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
# Uma solução alternativa, deixando a criatividade fluir =D
#         if not head:
#             return False
        
#         charVal = 97
#         while isinstance(head.val, int):
            
#             head.val = chr(charVal)
#             head = head.next
#             if head:
#                 res = head.val
#             else:
#                 res = chr(96)
#                 break
#             charVal = charVal + 1
        
#         res = ord(res) - 97
#         if res >= 0:
#             return True
#         else:
#             return False

    