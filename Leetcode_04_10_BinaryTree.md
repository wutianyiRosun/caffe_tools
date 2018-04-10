今天做的三道题105，107，112. 都是关于二叉树遍历。其中105，middle-level.

### 105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        if(preorder.size()==0)
            return NULL;
        TreeNode* root=(TreeNode*)malloc(sizeof(TreeNode));
        buildTreeCore(preorder, inorder, root);
        return root;
        
    }
    void  buildTreeCore(vector<int> preorder, vector<int> inorder, TreeNode* root){
        if(preorder.size()==1){
             root->val=preorder.at(0);
             root->left=NULL;
             root->right=NULL;
        }  
        else if (preorder.size()>1){ //多个节点
            root->val=preorder.at(0); //前序遍历中第一个为root Node
            vector<int> LeftSubTreePreorder,LeftSubTreeInorder, RightSubTreePreorder,RightSubTreeInorder;
            bool select=0; //0: 左子树序列
            for(int i=0; i<inorder.size();i++){
                if(inorder.at(i)!=preorder.at(0) && select==0){
                    LeftSubTreePreorder.push_back(preorder.at(i+1));
                    LeftSubTreeInorder.push_back(inorder.at(i));
                    
                }  
                else if(inorder.at(i)!=preorder.at(0)&& select==1){
                    RightSubTreePreorder.push_back(preorder.at(i));
                    RightSubTreeInorder.push_back(inorder.at(i));
                    
                }
                else  //root Node
                    select=1;
                
            }
            root->left=NULL;
            root->right=NULL;
            if(LeftSubTreePreorder.size()>0){
                TreeNode * LeftSubTreeRoot=(TreeNode*)malloc(sizeof(TreeNode));
                root->left=LeftSubTreeRoot;   
                buildTreeCore(LeftSubTreePreorder, LeftSubTreeInorder, LeftSubTreeRoot);
            }
                
            if(RightSubTreePreorder.size()>0){
                TreeNode * RightSubTreeRoot=(TreeNode*)malloc(sizeof(TreeNode));
                root->right=RightSubTreeRoot; 
                buildTreeCore(RightSubTreePreorder, RightSubTreeInorder, RightSubTreeRoot);
            }       
    
        }else{
        }

            
    }
};
```

### 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode *> ass_que;
        if(root!=NULL){
            ass_que.push(root);
            while(ass_que.empty()==0){
                vector<int> SubRes;
                int cur_levelNum=ass_que.size();
                for(int i=0;i<cur_levelNum; i++){
                    TreeNode* pcur=ass_que.front();
                    ass_que.pop();
                    if(pcur->left!=NULL){
                        ass_que.push(pcur->left);
                    }
                    if(pcur->right!=NULL){
                        ass_que.push(pcur->right);
                    }
                    SubRes.push_back(pcur->val);
                }
                //result.push_back(SubRes);
                result.insert(result.begin(),SubRes);
                SubRes.clear();  
            }
            
        }
        return result;
       
        
    }
};
```
### 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
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
    bool hasPathSum(TreeNode* root, int sum) {
        bool res=0;
        res=hasPathSumCore(root, sum);
        return res;
    }
    bool hasPathSumCore(TreeNode* root,int  sum){
           
            if(root==NULL)
                return false;
            if(root->right==NULL&&root->left==NULL&&sum==root->val)
                return true;
            return hasPathSumCore(root->left, sum-root->val) || hasPathSumCore(root->right,sum-root->val);
    }
};
```
