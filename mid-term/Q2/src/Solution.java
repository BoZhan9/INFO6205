import java.util.ArrayList;

public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(2);
        TreeNode n3 = new TreeNode(3);
        TreeNode n4 = new TreeNode(4);
        TreeNode n5 = new TreeNode(5);
        TreeNode n6 = new TreeNode(6);
        TreeNode n7 = new TreeNode(7);
        TreeNode n8 = new TreeNode(8);
        TreeNode n9 = new TreeNode(9);
        TreeNode n10 = new TreeNode(10);
        TreeNode n11 = new TreeNode(11);
        TreeNode n12 = new TreeNode(12);
        TreeNode n13 = new TreeNode(13);
        TreeNode n14 = new TreeNode(14);
        n1.left = n2;
        n1.right = n3;
        n2.left = n4;
        n2.right = n5;
        n3.left = n6;
        n4.right = n7;
        n5.left= n10;
        n5.right = n11;
        n6.right = n13;
        n7.left = n14;
        s.printPerimeter(n1);
        

    }
    public void printPerimeter(TreeNode root) {
        ArrayList<Integer> ans = new ArrayList<>(root.val);
        TreeNode node = root;
        while(node.right != null) {
            node = node.right;
            if (node.right != null) {
                ans.add(node.val);
            }
        }
        getAllLeafNodes(root);
        ans.addAll(res);
        node = root;
        ArrayList<Integer> rev = new ArrayList<>(root.val);
        while(node != null) {
            rev.add(node.val);
            node = node.left;
        }
        for(int i = rev.size() - 1; i >= 1; i--) {
            ans.add(rev.get(i));
        }
        System.out.println(ans);

    }
    ArrayList<Integer> res = new ArrayList<>();
    public void getAllLeafNodes(TreeNode root) {
        TreeNode node = root;
        if (node.left == null && node.right == null) {
            res.add(node.val);
            return;
        }
        getAllLeafNodes(root.right);
        getAllLeafNodes(root.left);
    }
}
