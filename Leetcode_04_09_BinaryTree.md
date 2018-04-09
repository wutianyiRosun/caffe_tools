今天做的三道题94，100，104都是关于二叉树的。

### 94. Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
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

//Recursive solution
/*
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodeset;
        inorderTraversalCore(root,nodeset);
        return nodeset;
    }
    
    void inorderTraversalCore(TreeNode* root, vector<int>& nodeset){
         if(root!=NULL){
             if(root->left!=NULL)
                 inorderTraversalCore(root->left, nodeset);
             nodeset.push_back(root->val);
             printf("cur_val=%d\t",root->val);
             if(root->right!=NULL)
                 inorderTraversalCore(root->right, nodeset);
        }   
    }
};*/
//iteratively solution, all TreeNode is pushed in ass_stack;
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodeset;
        if(root!=NULL){
            stack<TreeNode*> ass_stack;  
            TreeNode* pcur=root;
            while(pcur!=NULL||ass_stack.empty()==0){
                if(pcur!=NULL){ 
                    ass_stack.push(pcur);
                    pcur=pcur->left;
                    
                }
                else{
                    pcur=ass_stack.top();
                    ass_stack.pop();
                    nodeset.push_back(pcur->val);
                    pcur=pcur->right;
                } 
            }
 
        }
        return nodeset;
    }

};
```
### 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool flag=1;
        PreOrderTreeCore(p,q,flag); //递归式前序遍历两颗树，判断每个步骤节点的val是否相同，更快的方式应采用迭代法遍历
        return flag;
    }
    void PreOrderTreeCore(TreeNode* root1, TreeNode* root2, bool & flag){
        if(root1!=NULL&&root2!=NULL){
            if(root1->val!=root2->val){
                flag=0;
                return ;
            }
            PreOrderTreeCore(root1->left,root2->left,flag);
            PreOrderTreeCore(root1->right,root2->right,flag);
            
        }
        if((root1!=NULL&&root2==NULL)||(root1==NULL&&root2!=NULL)){
            flag=0;
        }
            
    }
};
```
### 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

return its depth = 3.

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
    int maxDepth(TreeNode* root) {//递归的思想
        
        if(root==NULL)
            return 0;
        int LchildDepth=maxDepth(root->left)+1;
        int RchildDepth=maxDepth(root->right)+1;
        return LchildDepth>RchildDepth?LchildDepth:RchildDepth;
        
        
    }
};
```
