# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val < p.val and root.val > q.val:
            return root
        if root.val > p.val and root.val < q.val:
            return root
        if root == p or root == q:
            return root
        if root.val > p.val and root.val > q.val:
             x = self.lowestCommonAncestor(root.left, p, q)
             return x 
        else: ##both p and q are bigger than root so now check traverse right subtree to find LCA
            x = self.lowestCommonAncestor(root.right, p, q)
            return x
        