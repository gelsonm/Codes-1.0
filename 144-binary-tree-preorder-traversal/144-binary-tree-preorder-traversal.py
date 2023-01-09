# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def pre(root):
            if root is None:
                return []
            return [root.val] + pre(root.left) + pre(root.right)
        
        return pre(root)
        