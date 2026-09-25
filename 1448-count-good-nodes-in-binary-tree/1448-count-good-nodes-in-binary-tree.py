# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c = 0
        # Here imp is that the maxi isnt global thus the maxi is always diiferent of left and right subtree!
        def counting(root,maxi):
            if not root:
                return
            
            if root.val >= maxi:
                self.c+=1
            
            maxi = max(maxi , root.val)
            
            counting(root.left , maxi)
            counting(root.right, maxi)
        
        counting(root, root.val)

        return self.c