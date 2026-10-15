# ALGORITHM: if the node is None return 0; otherwise find the depth of the
# left subtree and the right subtree, and return 1 (this node) + the larger.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftsteps = self.maxDepth(root.left)
        rightsteps = self.maxDepth(root.right)

        return 1 + max(leftsteps, rightsteps)


# ------------------------------------------------------------
# NOTES: issues in my original attempt
# ------------------------------------------------------------
# LOGIC
# 1. Left and right checks were in ONE if/elif chain. Only the first
#    matching branch of a chain runs, so once a left branch matched,
#    the right checks were skipped and rightsteps was never set.
#    Left and right are independent questions -> separate statements.
# 2. The +1 was in the wrong place. I added 1 per existing CHILD, so
#    a leaf returned max(0, 0) = 0 (counting edges, i.e. my notes'
#    height). LeetCode depth counts NODES (a leaf is 1), so the +1
#    belongs to the CURRENT NODE: return 1 + max(left, right).
# 3. The "node.left == None -> 0" checks were redundant. The base case
#    already returns 0 for None, so self.maxDepth(None) gives 0 for a
#    missing child automatically. Trust the base case.
#
# SYNTAX / STYLE
# 4. Extra space before "elif node.right == None:" -> IndentationError.
# 5. Use "is None", not "== None" (checks for exactly the None object).
# 6. node = root was an unnecessary alias. Use root directly.
# 7. The final if/elif comparison can be replaced by built-in max(a, b).
#
# UNDERSTANDING
# - This is POST-ORDER: get both children's answers first, then
#   combine them at the current node.
# - Pattern for most tree problems: base case for None, recurse on
#   left and right, combine the two results.
# - Complexity: O(n) time (each node visited once), O(h) space for
#   the recursion stack (h = tree height; O(n) worst case for a
#   lopsided tree, O(log n) for a balanced one).
# ------------------------------------------------------------