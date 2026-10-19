"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
##in this code we basically made a hash map called clones, where each original node is a key that point to (its value) its clone. We implement a recursive function within the method.

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:                     # empty graph: nothing to copy
            return None

        clones = {}                          # original node -> its clone (FIX 1 & 2)

        def clone(original):
            if original in clones:           # already copied: reuse that copy (stops infinite loops on cycles)
                return clones[original]

            copy = Node(original.val)        # new node, EMPTY neighbours list for now (FIX 3)
            clones[original] = copy          # record it BEFORE recursing, so cycles find it

            for neighbour in original.neighbors:          # FIX 4: loop gives Node objects, not indices
                copy.neighbors.append(clone(neighbour))   # FIX 5: use the returned clone to build the copy's neighbours

            return copy

        return clone(node)


# ------------------------------------------------------------
# NOTES: fixes to my original attempt
# ------------------------------------------------------------
# 1. A set only records THAT a node was seen. We also need to get back
#    the clone we already made for it, so we can link to it. That's a
#    dict: original -> clone (same idea as Two Sum: value -> index).
#
# 2. The set was created INSIDE cloneGraph, so every recursive call made
#    a fresh empty one and nothing was ever remembered. The dict must be
#    shared by all calls, so it lives outside the recursive helper.
#    (Keyed by the node OBJECT, not node.val, which is the safer habit.)
#
# 3. Node(node.val, node.neighbors) is a SHALLOW copy: the new node's
#    neighbours list IS the original list (aliasing, section 3.1), so it
#    still points at ORIGINAL nodes. Start with an empty list and fill it
#    with CLONES instead.
#
# 4. "for i in node.neighbors" gives each neighbour Node itself, so
#    node.neighbors[i] would crash. Use the loop variable directly.
#
# 5. The recursive call's result was thrown away (same bug as Lowest
#    Common Ancestor). The returned clone is exactly what goes into the
#    copy's neighbours list.
#
# ALSO: when the node was already done, nodeclone was never set, so
#    "return nodeclone" would crash. Now that case returns the stored clone.
#
# KEY LINE ORDER: add the copy to the dict BEFORE looping over the
# neighbours. Otherwise 1 -> 2 -> 1 would try to clone 1 again forever.
#
# Complexity: O(V + E). Each node is cloned once and each edge is
# followed once (twice for undirected). O(V) space for the dict.
# ------------------------------------------------------------

  



        


         