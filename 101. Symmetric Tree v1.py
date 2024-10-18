# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        l = root.left
        r = root.right

        def check_symmetry(l,r):
            
            if l == None and r == None:
                return True
            elif l == None or r == None:
                return False
            elif l.val != r.val:
                return False
            
            return check_symmetry(l.right,r.left) and check_symmetry(l.left,r.right)

        return check_symmetry(l,r)
