# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#this algorithm swaps the left and right pointers on every node in the tree, starting from the bottom up
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return None
        
        else: 
            lefttree = root.left 
            righttree = root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left = righttree
            root.right = lefttree
            return root
