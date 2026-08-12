# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        elif root.val == key:
            if root.right is None: return root.left
            cur = root.right
            k = TreeNode()
            while cur is not None:
                k = cur
                cur = cur.left
            k.left = root.left
            return root.right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
        


        

    #     9   
    # 4.      10
    #0  3    5.    8
