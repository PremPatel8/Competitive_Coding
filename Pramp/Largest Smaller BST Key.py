from typing import List

"""
Problem Name: Largest Smaller BST Key

Problem Section: Tree

Problem Statement:
Given a root of a Binary Search Tree (BST) and a number num, implement an
efficient function findLargestSmallerKey that finds the largest key in the
tree that is smaller than num. If such a number doesn’t exist, return -1.
Assume that all keys in the tree are nonnegative.
Analyze the time and space complexities of your solution.

Constraints:
[time limit] 5000ms
[input] Node rootNode
[output] integer


Resources:
"""

""" runtime """

# Solution techniques are

# Time complexity : O(log n) Space complexity : O(n)
""" Time Complexity: we scan the tree once from the root to the the leaves and do a 
constant number of actions for each node. if the tree is balanced the complexity is 
O(log(N)). Otherwise, it could be up to O(N).
Space Complexity: throughout the entire algorithm we used only a constant amount of space, 
hence the space complexity is O(1). """

##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# A binary search tree


class BinarySearchTree:

    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    def inorder(self, curr_node):
        if curr_node:
            self.inorder(curr_node.left)
            print(curr_node.key)
            self.inorder(curr_node.right)

    def height(self, node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            # Use the larger one
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

    # Print nodes at a given level
    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.key, end=" ")
        elif level > 1:
            self.printGivenLevel(root.left, level-1)
            self.printGivenLevel(root.right, level-1)

    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range(1, h+1):
            self.printGivenLevel(root, i)

    """ Iterative implementation """

    # def find_largest_smaller_key(self, num):
    #     res = -1
    #     currnode = self.root

    #     while currnode:
    #         if currnode.key <= num:
    #             res = currnode.key
    #             currnode = currnode.right
    #         else:
    #             currnode = currnode.left

    #     return res

    """ Recursive implementation """

    # def find_largest_smaller_key(self, num):
    #     res = -1
    #     currnode = self.root

    #     def helper(currnode):
    #         if not currnode:
    #             return -1
    #         if currnode.key == num:
    #             return num

    #         elif currnode.key < num:
    #             k = helper(currnode.right)
    #             if k == -1:
    #                 return currnode.key
    #             else:
    #                 return k
    #         elif currnode.key > num:
    #             return helper(currnode.left)

    #     res = helper(currnode)

    #     return res

    """ My Recursive solution """

    def find_largest_smaller_key(self, num):
        prev_node = None

        def inorder_sorted(curr_node):
            if curr_node:
                inorder_sorted(curr_node.left)

                if curr_node.key < num:
                    nonlocal prev_node
                    prev_node = curr_node
                else:
                    return prev_node.key

                inorder_sorted(curr_node.right)

        res = inorder_sorted(bst.root)

        return res

    """ Python 2.x sol nonlocal alternative solution """
    # def find_largest_smaller_key(self, num):
    #     d = {'prev_node' : None}

    #     def inorder_sorted(curr_node):
    #         if curr_node:
    #             inorder_sorted(curr_node.left)

    #             if curr_node.key < num:
    #                 d['prev_node'] = curr_node
    #             else:
    #                 return d['prev_node'].key

    #             inorder_sorted(curr_node.right)

    #     res = inorder_sorted(bst.root)
    #     return res

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):

        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)

        while(currentNode is not None):
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

#########################################
# Driver program to test above function #
#########################################


bst = BinarySearchTree()

# Create the tree given in the above diagram
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result = bst.find_largest_smaller_key(17)
print("Largest smaller number is %d " % (result))

# bst.inorder(bst.root)
# bst.printLevelOrder(bst.root)
