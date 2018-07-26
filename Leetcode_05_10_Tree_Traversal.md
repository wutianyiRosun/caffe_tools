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

//递归求解
/*
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorderTraversalCore(root, res);
        return res;
    }
    void preorderTraversalCore(TreeNode* root, vector<int> &res){
        //前序遍历， 先根节点，然后左子树，最后右子树
        if(root!=NULL){
            res.push_back(root->val);
            preorderTraversalCore(root->left, res);
            preorderTraversalCore(root->right, res);
        }
        
    }
};
*/

//前序遍历非递归实现
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode*> st;
        if (root==NULL) return res;
        
        TreeNode* pcur=root;
        while(pcur || !st.empty()){
            if(pcur){
                res.push_back(pcur->val);
                st.push(pcur);
                pcur=pcur->left;
            }
            else{
                TreeNode* node=st.top();
                st.pop();
                pcur=node->right;
            }
            
        }
        return res;
    }
};
/*
a)訪问之，并把结点node入栈。当前结点置为左孩子；
b)推断结点node是否为空，若为空。则取出栈顶结点并出栈，将右孩子置为当前结点；
否则反复a)步直到当前结点为空或者栈为空（能够发现栈中的结点就是为了訪问右孩子才存储的）
*/
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
