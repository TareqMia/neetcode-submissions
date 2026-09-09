# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0, True


            leftHeight, leftIsBalanced = dfs(root.left)
            rightHeight, rightIsBalanced = dfs(root.right) 


            isBalanced = abs(leftHeight - rightHeight) <= 1 and leftIsBalanced and rightIsBalanced

        
            return 1 + max(leftHeight, rightHeight), isBalanced 

        print(dfs(root))
        return dfs(root)[1]
        