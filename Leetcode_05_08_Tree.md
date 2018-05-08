### 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//判断一颗树是否为平衡树，我们得先计算出左右子树的高度，判断其相差是否小于等于1，然后判断左子树与右子树是否都是平衡的，当上述三个条件都满足，
//则整个树是平衡树
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(root == NULL) return true;
        int left = computeDepth(root->left);
        int right = computeDepth(root->right);
        return abs(left - right )<=1 && isBalanced(root->left) && isBalanced(root->right);
    }
    int computeDepth(TreeNode* root){
        if(root==NULL){
            return 0;
        }
        return max (computeDepth(root -> left), computeDepth((root -> right))) + 1;
    }
};

```
