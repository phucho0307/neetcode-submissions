# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def maxSearch(root: TreeNode, maxNum: int):
            if root is not None:
                if root.val >= maxNum: 
                    self.res +=1
                    maxNum = root.val
                maxSearch(root.left, maxNum)
                maxSearch(root.right,maxNum)
            return
        maxSearch(root, root.val)
        return self.res

#        3
#     1.     4
# 3        1    5
            
            


        
        