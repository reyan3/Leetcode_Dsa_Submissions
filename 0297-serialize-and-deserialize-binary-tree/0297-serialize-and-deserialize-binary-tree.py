# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def se(root):
            if not root:
                res.append("#")
                return
            
            res.append(str(root.val))

            se(root.left)
            se(root.right)

        se(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.index = 0

        def de():
            if values[self.index] == "#":
                self.index+=1
                return None
            
            root = TreeNode(int(values[self.index]))
            self.index+=1

            root.left = de()
            root.right = de()

            return root
        
        return de()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))