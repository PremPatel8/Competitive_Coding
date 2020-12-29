/* Binary Tree Maximum Path Sum

https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Resources:
https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram


Runtime:

 */

/* 
Solution technique is Postorder tree traversal with greedy choices
Time Complexity - O(n)
Space Complexity - O(1)
 */

/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
class Solution {
    int max_path_value = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        getMaxGain(root);

        return max_path_value;
    }

    private int getMaxGain(TreeNode node) {
        if (node == null)
            return 0;

        int left_gain = Math.max(0, getMaxGain(node.left));
        int right_gain = Math.max(0, getMaxGain(node.right));

        int current_max_path = node.val + left_gain + right_gain;

        max_path_value = Math.max(max_path_value, current_max_path);

        return node.val + Math.max(left_gain, right_gain);
    }
}