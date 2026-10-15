# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        leftcheck = self.isSameTree(p.left, q.left)
        if not leftcheck:
            return False
        rightcheck = self.isSameTree(p.right, q.right)
        return rightcheck


# ------------------------------------------------------------
# NOTES: issues in my original attempt
# ------------------------------------------------------------
# LOGIC
# 1. Base case checked node.val == None instead of node is None.
#    An empty tree/branch is the NODE being None, not its value.
#    At the bottom of a branch the node is None, so .val crashes
#    (None has no attributes).
# 2. Missing case: exactly one node is None (e.g. p has a left child,
#    q doesn't). The trees have different shapes -> return False.
#    The "p is None or q is None" check handles this. It only runs
#    after the "both None" check, so here it means EXACTLY one is None.
# 3. Right check compared node1.right with node2.LEFT (typo). That
#    tests whether one tree is a mirror of the other, not identical.
# 4. If leftcheck failed, nothing was returned (implicit None).
#    Every path should return an explicit True or False.
#
# SYNTAX
# 5. Recursive calls need self.isSameTree(...). It's a method inside
#    the Solution class, so a bare isSameTree(...) gives a NameError.
# 6. if leftcheck = True: used = (assignment) instead of ==
#    (comparison). Better still, use truthiness: if leftcheck:
# 7. node1 = p and node2 = q were unnecessary extra names (aliases
#    for the same objects). Use p and q directly.
#
# UNDERSTANDING
# - p and q are the ROOT NODES of the two trees (TreeNode or None).
#   The [1,2,3] arrays on NeetCode are only how inputs are displayed.
# - A missing child is None (TreeNode defaults left/right to None).
# - Order of checks matters: handle None BEFORE touching .val.
# - Complexity: O(n) time (each node visited at most once),
#   O(h) space for the recursion stack (h = tree height).
# ------------------------------------------------------------

        

        