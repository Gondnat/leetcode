# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        resultIter = result
        needUpper = False
        while True:
            resultIter.val = (l1.val if l1 !=None else 0) + (l2.val if l2 != None else 0) + (1 if needUpper else 0)
            if resultIter.val >= 10:
                resultIter.val -= 10
                needUpper = True
            if l1.next != None and l2.next != None:
                resultIter.next = ListNode()
                resultIter = resultIter.next
                l1 = l1.next
                l2 = l2.next
            else:
                break
        
        return result
        

def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while result != None:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()