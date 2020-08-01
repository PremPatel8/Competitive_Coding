from typing import List

"""
Problem Name: Serialize and Deserialize Binary Tree

Problem Section: Design

Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or 
memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Resources:

"""

""" 48 / 48 test cases passed.
	Status: Accepted
Runtime: 108 ms
Memory Usage: 18.4 MB """
# Solution techniques are

# Time complexity : O() Space complexity : O()


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        sent = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            sent.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(sent)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        received = data.split(',')
        root = TreeNode(received[0])
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if received[i] != '#':
                node.left = TreeNode(received[i])
                queue.append(node.left)
            i += 1
            if received[i] != '#':
                node.right = TreeNode(received[i])
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


myobj = Codec()
inpt = [10, 9, 2, 5, 3, 7, 101, 18]
print(myobj.serialize(inpt))
print(myobj.deserialize(inpt))
