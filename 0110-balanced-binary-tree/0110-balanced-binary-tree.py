# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dot(root):
            if not root:
                return 0

            l = dot(root.left)
            if l == -1:
                return -1
            r = dot(root.right)
            if r == -1:
                return -1

            if abs(l - r) > 1:
                return -1

            return 1 + max(l, r)

        return dot(root) != -1
