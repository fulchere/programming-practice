class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    if l1.val < l2.val:
        main = l1
        pull_in = l2
    else:
        main = l2
        pull_in = l1

    return_head = main
    while main is not None and pull_in is not None:
        if pull_in is not None and pull_in.val >= main.val and main.next is None:
            main.next = pull_in
            return return_head

        if pull_in is not None and pull_in.val >= main.val and pull_in.val <= main.next.val:
            temp = pull_in.next
            pull_in.next = main.next
            main.next = pull_in
            pull_in = temp

        main = main.next
        if main.next is None and pull_in is not None:
            main.next = pull_in
            return return_head

    return return_head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(4)
n1.next = n2
n2.next = n3
n4 = ListNode(1)
n5 = ListNode(3)
n6 = ListNode(4)
n4.next = n5
n5.next = n6

n = mergeTwoLists(n1, n4)
while n is not None:
    if n.next is not None:
        print(n.val, '=> ', end='')
    else:
        print(n.val)
    n = n.next
