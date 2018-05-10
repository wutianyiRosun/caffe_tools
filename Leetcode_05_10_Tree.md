### 144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.
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
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorderTraversalCore(root, res);
        return res;
    }
    void preorderTraversalCore(TreeNode* root, vector<int> &res){
        //前序遍历， 先根节点，然后左儿子，最后右儿子
        if(root==NULL) return;
        res.push_back(root->val);
        if(root->left!=NULL)
            preorderTraversalCore(root->left, res);
        if(root->right!=NULL)
            preorderTraversalCore(root->right, res);
        
    }
};
```
