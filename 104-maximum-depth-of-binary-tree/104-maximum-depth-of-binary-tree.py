# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if(root is None):
            return 0
        else:
            left_Height = self.maxDepth(root.left)
            right_Height = self.maxDepth(root.right)
            return max(left_Height, right_Height)+1
        
        