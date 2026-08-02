# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dmax = 0
        def dia(root):
            if root is None: return 0
            l = 0
            if root.left is not None:
                l = dia(root.left) + 1
            r = 0
            if root.right is not None:    
                r = dia(root.right) + 1
            curr = l+r
            self.dmax = max(self.dmax, curr)
            return max(l,r) 
        dia(root)
        return self.dmax

        