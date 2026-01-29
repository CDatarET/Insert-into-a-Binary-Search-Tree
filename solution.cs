public class Solution {
    private void helper(TreeNode root, int val){
        if(val < root.val){
            if(root.left == null){
                root.left = new TreeNode(val, null, null);
            }
            else{
                helper(root.left, val);
            }
        }
        else{
            if(root.right == null){
                root.right = new TreeNode(val, null, null);
            }
            else{
                helper(root.right, val);
            }
        }
    }

    public TreeNode InsertIntoBST(TreeNode root, int val) {
        if(root == null){
            return(new TreeNode(val, null, null));
        }

        helper(root, val);
        return(root);
    }
}
