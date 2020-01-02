#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode(-1)
        p.next = head
        res = p
        q = p.next
        while q:
            if q.val == val:
                p.next = q.next
            else:
                p = p.next
            q = q.next
        return res.next
# @lc code=end

