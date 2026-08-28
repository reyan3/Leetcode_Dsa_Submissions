# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def sametree(p,q):
            if not q and not p:
                return True
            
            if not q or not p:
                return False
            
            if p.val != q.val:
                return False
            
            return (sametree(p.left,q.left) and sametree(p.right,q.right))
        
        if sametree(root,subRoot):
            return True
        
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        
        
            
            

