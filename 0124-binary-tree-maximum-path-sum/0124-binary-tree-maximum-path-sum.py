# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi = root.val

        def totalSum(root):
            if not root:
                return 0
            
            left = max(0 , totalSum(root.left))
            right = max(0 , totalSum(root.right))

            self.maxi = max(self.maxi , root.val + left + right)

            return root.val + max(left,right)
        
        totalSum(root)
    
        return self.maxi
        