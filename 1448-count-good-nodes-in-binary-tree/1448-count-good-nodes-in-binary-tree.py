# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        maxi = 0

        def countVal(root, maxi):
            if not root:
                return 0
            
            if root.val >= maxi:
                self.cnt += 1
            
            maxi = max(maxi , root.val)

            countVal(root.left , maxi)
            countVal(root.right , maxi)
        
        countVal(root , root.val)
        
        return self.cnt