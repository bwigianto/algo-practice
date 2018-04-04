import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, obj):
        return isinstance(obj, ListNode) and self.val == obj.val and self.next == obj.next

def listnode(arr):
    head = ListNode(arr[0])
    prev = head
    for v in arr[1:]:
        curr = ListNode(v)
        prev.next = curr
        prev = curr
    return head

def tostring(l):
    s = '['
    while l:
        s += str(l.val) + ','
        l = l.next
    return s + ']'

class AddTwoTest(unittest.TestCase):

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(None)
        prev = head
        while l1 and l2:
            v = l1.val + l2.val + carry
            carry = 1 if v >= 10 else 0
            curr = ListNode(v % 10)
            prev.next = curr
            prev = curr
            l1 = l1.next
            l2 = l2.next
        while l1:
            v = l1.val + carry
            carry = 1 if v >= 10 else 0
            curr = ListNode(v % 10)
            prev.next = curr
            prev = curr
            l1 = l1.next
        while l2:
            v = l2.val + carry
            carry = 1 if v >= 10 else 0
            curr = ListNode(v % 10)
            prev.next = curr
            prev = curr
            l2 = l2.next
        if carry > 0:
            prev.next = ListNode(carry)
        return head.next

    def test_add_two(self):
        self.assertEqual(self.addTwoNumbers(listnode([2, 4, 3]), listnode([5, 6, 4])), listnode([7, 0, 8]))

    def test_add_two_with_carry(self):
        self.assertEqual(self.addTwoNumbers(listnode([2, 4, 8]), listnode([5, 6, 4])), listnode([7, 0, 3, 1]))

    def test_one_larger(self):
        self.assertEqual(self.addTwoNumbers(listnode([2, 4, 3, 7, 8]), listnode([5, 6, 4])), listnode([7, 0, 8, 7, 8]))
        self.assertEqual(self.addTwoNumbers(listnode([5, 6, 4]), listnode([2, 4, 3, 7, 8])), listnode([7, 0, 8, 7, 8]))
if __name__ == '__main__':
    unittest.main()
