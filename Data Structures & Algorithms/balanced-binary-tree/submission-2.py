# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.k=0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(right-left)>1: 
                self.k=-1
                
            return 1 + max(left,right)
        dfs(root)
        if self.k == -1: return False
        else: return True

        