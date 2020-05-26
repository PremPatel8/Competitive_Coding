from binarytree import tree, bst


def checkBST(root):
    nodes = []

    def InOrder(node):
        if node.left:
            InOrder(node.left)

        nodes.append(node.val)

        if node.right:
            InOrder(node.right)

    InOrder(root)

    uniqueNodes = set(nodes)

    if len(nodes) == len(uniqueNodes):
        if sorted(nodes) == nodes:
            return True
        else:
            return False
    else:
        return False


tree = bst(is_perfect=True)

print(tree)

print(checkBST(tree))
