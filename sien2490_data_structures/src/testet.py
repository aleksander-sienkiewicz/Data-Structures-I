"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-04-14"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
class Node:
        def __init__(self, key):
                self.key = key
                self.left = None
                self.right = None

class BST:
        def __init__(self):
                self.root = None

        def insert(self, key):
                self.root = self._insert_helper(self.root, key)

        def _insert_helper(self, root, key):
                if(root is None):
                        return Node(key)

                if(root.key < key):
                        root.right = self._insert_helper(root.right, key)
                else:
                        root.left = self._insert_helper(root.left, key)

                return root

        def show(self):
                self._show_helper(self.root)
                print()

        def _show_helper(self, root):
                if(root is None):
                        return

                self._show_helper(root.left)
                print(root.key, end = ' ')
                self._show_helper(root.right)

        # method to change tree to its mirror image
        def mirror(self):
                # call helper method
                self._mirror_aux(self.root)


        def _mirror_aux(self, root):
                # if tree is empty
                if(root is None):
                        return
                # swap current node's left and right child
                root.left, root.right = root.right, root.left

                # make recursive call for left and right subtree
                self._mirror_aux(root.left)
                self._mirror_aux(root.right)


tree = BST()
for i in [10, 30, 5, 3, 25, 35]:
        tree.insert(i)

tree.show()
tree.mirror()
tree.show()
