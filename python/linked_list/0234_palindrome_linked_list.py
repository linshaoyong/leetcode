# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        values = []
        while node:
            values.append(node.val)
            node = node.next
        length = len(values)
        for i in range(0, length // 2):
            if values[i] != values[length - i - 1]:
                return False
        return True


def test_is_palindrome():
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    assert Solution().isPalindrome(a) is False

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    assert Solution().isPalindrome(a) is True
