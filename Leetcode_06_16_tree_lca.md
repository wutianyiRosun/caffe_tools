### 236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.

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
//step1.前序遍历找出p和q的路径path_p, path_q, 二者为队列
//让两个队列都进行元素出队操作，找到最后一次出队的两个相同相同元素， 该元素就是LCA
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* lca=NULL;
        if(root==NULL || root==p || root==q)
            return root;
        deque<TreeNode*> path_p, path_q;
        // find path for node p and node q
        bool find1=FindNodePath(root, p, path_p);
        bool find2=FindNodePath(root, q, path_q);
        // get Last common node of two path
        lca= GetLastCommonNode(path_p, path_q);
        return lca;
        
    }
    TreeNode * GetLastCommonNode(deque<TreeNode*> & path_p, deque<TreeNode*> & path_q){
        TreeNode * lca=NULL;
        auto iter_p=path_p.begin();
        auto iter_q=path_q.begin();
        while(iter_p!=path_p.end() && iter_q!=path_q.end() ){
           if(*iter_p == *iter_q){
               lca=*iter_p; //对iter进行解引用，返回迭代器iter指向的元素的引用
               cout<<lca<<"  "<<lca->val<<" "<<*iter_p<<endl;
           }
           iter_p++;
           iter_q++;
        }
        return lca;
    }
    bool FindNodePath(TreeNode* root, TreeNode *p, deque<TreeNode*> & path){
        //stack<TreeNode*> traverse; 
        path.push_back(root);
        if(root ==p){
            return true;
        }
        bool Found=false;
        
        if(Found==false && root->left!=NULL){
            Found=FindNodePath(root->left,  p, path);
        }
        if(Found==false && root->right!=NULL){
            Found=FindNodePath(root->right, p, path);
        }
        if(Found==false)
            path.pop_back();
        return Found;
           
    }
    
};
```
### 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
```
//对于长度为N的序列， 任意的i, 我们计算output[i]=nums[0,...,i-1]左边序列乘积用Lprod[i]表示 与 右边序列nums[i+1,...,N-1],用Rprod[i]表示
//output[i]=Lprod[i]*Rprod[i];

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        //computing Lrpod[i]
        int len=nums.size();
        int Lprod[len]; //Lprod[i]表示nums[0,...,i-1]子序列所有元素的乘积
        Lprod[0]=1;
        for(int i=1; i<len; i++){
            Lprod[i]=Lprod[i-1]*nums[i-1];
        }
        int Rprod[len];  //Rprod[i]表示子序列nums[i+1, ..., N-1]所有元素乘积
        Rprod[len-1]=1;
        for(int i=len-2; i>=0; i--){
            Rprod[i]=Rprod[i+1]*nums[i+1];
        }
        vector<int> output(len, 0);
        for(int i=0;i<len;i++){
            output[i]=Lprod[i]*Rprod[i];
        }
        return output;
    }
};
```
