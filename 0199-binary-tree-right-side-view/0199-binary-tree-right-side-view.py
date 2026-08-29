# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        # Here we used to insert right first rather than left so that i==0
        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
                
                if i==0:
                    res.append(node.val)
        return res
            
