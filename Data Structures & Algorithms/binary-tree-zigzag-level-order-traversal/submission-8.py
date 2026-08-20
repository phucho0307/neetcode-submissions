# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        k = 0
        while queue:
            l = len(queue)
            level = []
            for _ in range (l):
                node = queue.popleft()
                level.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if k==0:
                result.append(level)
                k=1
            elif k==1:
                level.reverse()
                result.append(level)
                k=0
        return result


                
                