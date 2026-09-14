# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        d = {}

        for i in range(len(inorder)):
            d[inorder[i]] = i
        
        def build(preStart , preEnd , inStart , inEnd):

            if preStart > preEnd or inStart > inEnd:
                return None
            
            rootval = preorder[preStart]
            root = TreeNode(rootval)

            inRoot = d[rootval]

            numsleft = inRoot - inStart

            root.left = build(preStart + 1 , preStart + numsleft , inStart , inRoot - 1)

            root.right = build(preStart + numsleft + 1 , preEnd , inRoot + 1 , inEnd)
            
            return root

        return build(0 , len(preorder)-1 , 0 , len(inorder)-1)
        
        
        