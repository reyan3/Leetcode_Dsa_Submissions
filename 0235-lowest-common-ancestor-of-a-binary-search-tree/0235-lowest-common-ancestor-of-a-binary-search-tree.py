# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            
            # as in bst all left value is lower than root value
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # as in bst all right value is greater than root value
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # if not greater or smaller value found then the intersection is always the root therefore return root
            else:
                return root