# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## algorithm that checks if node itself exists (if not just returns None). then if left node exists, if it does then recursively calls its self on left node, appends that result to a list, then appends itself and does same check and then recusive call on right node 

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ##returning nothing if the node doesn't exist 
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
            

        
        
          

        