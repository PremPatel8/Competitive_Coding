from binarytree import tree, bst

def checkBST(root):
    nodeList = []

    def InOrder(node):
        if node.left:
            InOrder(node.left)

        nodeList.append(node.val)

        if node.right:
            InOrder(node.right)
    
    InOrder(root)
    
    return sorted(list(set(nodeList))) == nodeList


tree = bst(is_perfect=True)

# print(tree)

print(checkBST(tree))
