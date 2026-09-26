# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        d = {}

        for i,n in enumerate(inorder):
            d[n] = i
        
        def build(preSt , preEnd , inSt , inEnd):
            if preSt > preEnd or inSt > inEnd:
                return None
            
            rootval = preorder[preSt]
            root = TreeNode(rootval)

            inRoot = d[rootval]
            numsleft = inRoot - inSt

            root.left = build(preSt + 1 , preSt+numsleft , inSt , inRoot-1)
            root.right = build(preSt + numsleft + 1 , preEnd , inRoot+1 , inEnd)

            return root
        
        return build(0, len(preorder)-1, 0 , len(inorder) - 1)