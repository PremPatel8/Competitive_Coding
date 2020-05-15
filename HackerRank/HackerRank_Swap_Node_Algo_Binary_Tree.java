import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    node tree[];
    ArrayList<Integer> depth[];

    /*
     * Complete the swapNodes function below.
     */
    static int[][] swapNodes(int[][] indexes, int[] queries) {
        int [][] resultvalues
        int n = indexes.length;
        tree = new node[n + 1];
        depth = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            tree[i] = new node(i);
            depth[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n; i++) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            if (l != -1) {
                tree[i].left = tree[l];
            }
            if (r != -1) {
                tree[i].right = tree[r];
            }
        }

        dfs(tree[1], 1);

        System.out.println("depth "+ Arrays.toString(depth));

        int t = queries.length;

        while (t-- > 0) {
            int k = queries[t];
            int h = k;
            while (h <= n) {
                // swap children of each node at depth h
                for (int d : depth[h]) {
                    node temp = tree[d].left;
                    tree[d].left = tree[d].right;
                    tree[d].right = temp;
                }
                // h is all the possible multiples of k where we have to swap nodes
                h += k;
            }
            inorder(tree[1], t);
            // System.out.println();
        }
        return resultvalues
    }

    void inorder(node t, int x) {
        if (t == null) return;
        inorder(t.left);
        // System.out.print(t.data + " ");
        resultvalues[x].append(t.data);
        inorder(t.right);
    }

    void dfs(node t, int y) {
         if (t == null) return;
        // add node label (at depth y) to the arraylist depth at index y
        depth[y].add(t.data);
        dfs(t.left, y + 1);
        dfs(t.right, y + 1);
    }

    class node {
        node left, right;
        int data;

        node(int x) {
            this.data = x;
            this.left = this.right = null;
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(scanner.nextLine().trim());

        int[][] indexes = new int[n][2];

        for (int indexesRowItr = 0; indexesRowItr < n; indexesRowItr++) {
            String[] indexesRowItems = scanner.nextLine().split(" ");

            for (int indexesColumnItr = 0; indexesColumnItr < 2; indexesColumnItr++) {
                int indexesItem = Integer.parseInt(indexesRowItems[indexesColumnItr].trim());
                indexes[indexesRowItr][indexesColumnItr] = indexesItem;
            }
        }

        int queriesCount = Integer.parseInt(scanner.nextLine().trim());

        int[] queries = new int[queriesCount];

        for (int queriesItr = 0; queriesItr < queriesCount; queriesItr++) {
            int queriesItem = Integer.parseInt(scanner.nextLine().trim());
            queries[queriesItr] = queriesItem;
        }

        int[][] result = swapNodes(indexes, queries);

        for (int resultRowItr = 0; resultRowItr < result.length; resultRowItr++) {
            for (int resultColumnItr = 0; resultColumnItr < result[resultRowItr].length; resultColumnItr++) {
                bufferedWriter.write(String.valueOf(result[resultRowItr][resultColumnItr]));

                if (resultColumnItr != result[resultRowItr].length - 1) {
                    bufferedWriter.write(" ");
                }
            }

            if (resultRowItr != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();
    }
}
