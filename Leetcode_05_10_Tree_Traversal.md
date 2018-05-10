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
/*
//递归求解
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
*/
//循环实现
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        if (root==NULL) return res;
        st.push(root);
        TreeNode* pcur;
        while(!st.empty()){
            pcur=st.top();
            st.pop();
            while(pcur!=NULL){
                res.push_back(pcur->val);
                st.push(pcur->right);
                pcur=pcur->left;
            }
            
        }
        return res;
    }
   
};
```
### 145. Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.
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
//递归实现
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        postorderTraversal(root, res);
        return res;
    }
    void postorderTraversal(TreeNode* root, vector<int> & res){
        if(root==NULL) return;
        //后序遍历， 先左儿子再右儿子最后根节点
        if(root->left)
            postorderTraversal(root->left, res);
        if(root->right)
            postorderTraversal(root->right, res);
        res.push_back(root->val);
    }
};
```
