# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None #edge case

        # swap the root right and left
        temp = root.left
        root.left = root.right
        root.right = temp

        # use recursion for DFS 
        self.invertTree(root.left) #first go to left parent
        self.invertTree(root.right) #after that go to right parent
        return root #return inverted root
