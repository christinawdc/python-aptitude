class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            elif left.val!=right.val:
                return False
            return mirror(left.left,right.right) and mirror (right.left,left.right)
        return mirror(root.left,root.right)
