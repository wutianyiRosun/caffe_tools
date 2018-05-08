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

### 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

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
//对于判断对称树，我们只需要判断其左子树和右子树是否Mirror，因此我们的问题转换成了如果判断两颗树是否为mirror.通过画图举出实际例子可以
//总结出，两颗树互为mirror的条件是两颗树的根节点value相等，然后树1的左子树与树2的右子树互为Mirror,树1的右子树与树2的左子树互为Mirror
//当这三个条件都成立，原树是对称的
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root==NULL) return true;
        return isMirror(root->left, root->right);
        
    }
    bool isMirror(TreeNode * root1, TreeNode* root2){
        if (root1==NULL && root2 == NULL)
            return true;
        if(root1==NULL|| root2==NULL)
            return false;
        return ( root1->val == root2->val && isMirror(root1->left, root2->right) && isMirror(root1->right, root2->left));
    }
};
```



