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
        coded = []

        def dfs(root):
            if not root:
                coded.append("#")
                return
            coded.append(str(root.val))
            dfs(root.left)
            dfs(root.right)



        dfs(root)
        return ",".join(coded)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        traversal = data.split(",")
        print(traversal)

        def dfs(t):
            if t[0] == "#":
                t.pop(0)
                return None 

            root = TreeNode(t[0])
            t.pop(0)

            root.left = dfs(t)
            root.right = dfs(t)
            return root

        return dfs(traversal)


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))