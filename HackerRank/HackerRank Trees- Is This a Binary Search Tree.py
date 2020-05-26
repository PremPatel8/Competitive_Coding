from binarytree import bst
import sys


# Recursive solution
def checkBST(root):

    def _checkBST(node, mi, mx):
        if node is None:
            return True

        return (mi < node.val and node.val < mx) and (
            _checkBST(node.left, mi, node.val) and
            _checkBST(node.right, node.val, mx))

    return _checkBST(root, -sys.maxsize - 1, sys.maxsize)


tree = bst(is_perfect=True)

print(tree)

print(checkBST(tree))
