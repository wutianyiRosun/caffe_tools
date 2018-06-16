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
