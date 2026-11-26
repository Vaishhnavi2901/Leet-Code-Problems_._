class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.head = head
        def get_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            left_child = build(left, mid - 1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left_child
            root.right = build(mid + 1, right)

            return root

        n = get_length(head)
        return build(0, n - 1)
        