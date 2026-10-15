# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## ALGORITHM (in-order: left, node, right): if the node doesn't exist return [];
## otherwise recurse on the left subtree, add the current node's value, then
## recurse on the right subtree, and return the combined list.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ##returning an empty list if the node doesn't exist
        if root == None:
            return []

        ##node exists, so now need to check its branches
        elif root != None:
            traversed = []

            ## recursive call on left, then adding current value
            traversed.extend(self.inorderTraversal(root.left))
            traversed.append(root.val) #noting current node
            ## recursive call on the right
            traversed.extend(self.inorderTraversal(root.right))

            return traversed


# ------------------------------------------------------------
# NOTES: main issues implementing my algorithm
# ------------------------------------------------------------
# 1. I checked whether the left/right child existed BEFORE making the
#    recursive call. Unnecessary: the base case already returns [] for
#    None, so calling on a missing child just gives back an empty list,
#    and extending by [] adds nothing. Trust the base case and always
#    recurse on both children (same lesson as Max Depth).
#
# 2. I used append to add the result of the recursive calls. append adds
#    its argument as ONE element, so a returned list got nested inside
#    mine: [1].append([2, 3]) -> [1, [2, 3]]. extend adds each element
#    individually: [1].extend([2, 3]) -> [1, 2, 3].
#    Rule of thumb: append for a single value (root.val), extend (or +)
#    for adding another list's contents (the recursive results).
#
# MINOR: the "elif root != None" is redundant. If the first if didn't
# return, root can't be None, so the code can just carry on unindented.
#
# Complexity: O(n) time (each node visited once), O(h) recursion space.
# Run it on a BST and the output comes out in sorted order.
# ------------------------------------------------------------

        
        
          

        