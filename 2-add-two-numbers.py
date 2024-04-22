# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.listNode3 = ListNode()
        self.current = self.listNode3
        self.carry = 0
        self._l1 = l1
        self._l2 = l2

        while self._l1 or self._l2:
            sum = self.carry
            if self._l1:
                sum += self._l1.val
                self._l1 = self._l1.next

            if self._l2:
                sum += self._l2.val
                self._l2 = self._l2.next

            temp = sum % 10

            if sum > 9:
                self.carry = 1
            else:
                self.carry = 0
            
            self.current.next = ListNode(temp)
            self.current = self.current.next

        if self.carry:
            self.current.next = ListNode(self.carry)
        
        return self.listNode3.next
