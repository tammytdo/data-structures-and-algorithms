def mergeLists(self, list2):
    head1 = self.head
    head2 = self.head
    if not head1 and not head2:
        return 'empty linked list'
    if head1 and not head2:
        return head1
    if not head1 and head2:
        return head2
    if head1 and head2:
        curr1 = head1
        curr2 = head2
        while curr1._next is not None and curr2._next is not None:
            ref1 = curr1._next
            ref2 = curr2._next
            curr1._next = curr2
            curr2._next = ref1
            curr1 = ref1
            curr2 = ref2
        if curr1._next is None and curr2:
            curr1._next = curr2
            return head1
        if curr2._next is None and curr1:
            ref1 = curr1._next
            curr1.next = curr2
            curr2.next = ref1
            return head1