class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        while ptr is not None and ptr.next is not None:
            if ptr.next.val==ptr.val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head
