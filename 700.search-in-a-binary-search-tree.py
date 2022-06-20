'''
Solution 1: Iterative approach 
-> we check if there is a root in the first place, if not, we return none. 
-> then, while a root node exists, 
we check if the value given is less than the root node value, 
if yes -> we move the root to the left (left subtree), similarly we 
see if the value given is greater than the root node value, 
if yes -> we move the root to the right (right subtree)
now if the root.val and val are equal (else condition) ==> return the root.
'''

class Solution(object):
    def searchBST(self, root, val):

        if not root: return None
        while root:
            if val<root.val: root = root.left
            elif val>root.val: root = root.right
            else: return(root)