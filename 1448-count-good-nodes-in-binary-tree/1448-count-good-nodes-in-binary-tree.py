# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0 
        # Store maximum and then count values which are greater than maximum
        def count(root,maxi):
            if not root:
                return None
            
            if root.val >= maxi:
                self.cnt += 1
            
            maxi = max(maxi , root.val)

            count(root.left, maxi)
            count(root.right, maxi)
        
        count(root,root.val)
        return self.cnt
        
