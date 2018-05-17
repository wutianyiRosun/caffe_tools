### 655. Print Binary Tree
Print a binary tree in an m*n 2D string array following these rules:

    The row number m should be equal to the height of the given binary tree.
    The column number n should always be an odd number.
    The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
    Each unused space should contain an empty string "".
    Print the subtrees following the same rules.
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
     int maxDepthOfTree(TreeNode* root){
        if(root==NULL)
            return 0;
        int ldepth= maxDepthOfTree(root->left)+1;
        int rdepth= maxDepthOfTree(root->right)+1;
        return max(ldepth, rdepth);
    }
    void populateRes(TreeNode* root, vector<vector<string>>& res, int r, int l, int h) {
        if (root == nullptr) {
            return;
        }
        int mid = l + (h-l)/2;
        populateRes(root->left, res, r + 1, l, mid - 1);
        populateRes(root->right, res, r + 1, mid + 1, h);
        res[r][mid] = to_string(root->val);
        
    }
    vector<vector<string>> printTree(TreeNode* root) {
        int height = maxDepthOfTree(root);
        int c = (1 << height) - 1;
        vector<vector<string>> res(height, vector<string>(c));
        cout<<"matrix.shape: "<<height<<"-"<<c<<endl;
        populateRes(root, res, 0, 0, c);
        return res;
    }
};
```
### 111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
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
    int minDepth(TreeNode* root) {
        if(root==NULL)
            return 0;
        int ldepth = minDepth(root->left)+1;
        int rdepth = minDepth(root->right)+1;
        if(root->left==NULL)
            return rdepth;
        if(root->right==NULL)
            return ldepth;
        return min(ldepth, rdepth);
    }
};
```
### 102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int>> res;
        if(!root)
            return res;
        queue<TreeNode*> treeQueue;
        treeQueue.push(root);
        int curlevel=1;   //node numbers of current level
        int nextlevel=0; //node numbers of next level
        vector<int> restemp;
        while(treeQueue.empty()!=1){
            TreeNode * pcur = treeQueue.front();
            if(pcur->left){
                treeQueue.push(pcur->left);
                nextlevel++;
            }
            if(pcur->right){
                treeQueue.push(pcur->right);
                nextlevel++;
            }  
            restemp.push_back(pcur->val);
            curlevel-=1;
            treeQueue.pop();
            if(curlevel==0){
                res.push_back(restemp);
                for(auto iter=restemp.begin(); iter!=restemp.end(); )
                    iter=restemp.erase(iter);
                curlevel=nextlevel;
                nextlevel=0;
            }   
        }
        return res;
        
    }
};
```

