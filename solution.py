# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val, None, None)
            else:
                self.helper(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val, None, None)
            else:
                self.helper(root.right, val)

    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val, None, None)
        
        self.helper(root, val)
        return root
