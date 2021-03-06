### 235. Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

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
//Solution1: 首先遍历p节点的路径和q节点的路径，分别保存到两个queue,然后从队列开始出队元素，最后一个相同的元素则是我们要找的最低公共祖先
//Solution2： 对于二叉搜索树两个节点的最低公共祖先， 假设我们拿到一颗BSTree的根节点，如果根节点的值都小于p和q的值，则最低公共祖先在其右子树，
//如果大于p和q的值则最低公共祖先在其左子树，否则最低公共祖先就是当前这个根节点。 然后递归。（当然前提是给的两个节点p和q都在这个树上） 
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while(root!=p && root!=q){
            if(root->val < p->val && root->val < q->val){
                root=root->right;
            }
            else if(root->val > p->val && root->val > q->val){
                root= root ->left;
            }
            else
                break;
        }
        return root;
    
    }
};
```
### 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
//对与tree路径遍历，采用递归烦死解决非常容易处理，对于一个节点，如果它是非空的叶子节点，我们则把当前路径保存到paths,如果它左儿子不为空，
//我们则递归遍历它左子树，如果它右儿子不为空，我们则递归遍历它右子树。
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> paths; //all pths
        vector<int> spath;  //single path
        FindPath(root, paths, spath);
        return paths;
    }
    void FindPath(TreeNode* root, vector<string> & paths, vector<int> spath){
        if(root==NULL || root->val==NULL) return;
        spath.push_back(root->val);
        if(root->left!=NULL){
            
            FindPath(root->left, paths, spath);
        }
        if(root->right!=NULL){
            FindPath(root->right, paths, spath);
        }
        if(root->left == NULL && root->right == NULL && root->val!=NULL){  //非空叶子节点
            string pathstr;
            for(int i=0;i<spath.size(); i++){
                pathstr+=to_string(spath[i]);
                if(i+1 < spath.size())
                    pathstr+="->";
            }
            paths.push_back(pathstr);
        }

    }
};
```

### 671. Second Minimum Node In a Binary Tree
 Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead. 

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
//对于查找第二小的值，我们可以利用一个优先队列来保存大于根的值（数值小的优先级高），取遍历整个树
//如果最后优先队列不为空，且最小的元素大于根节点的值,则这个最小的元素就是第二小值，否则不存在第二小的值
class Solution {
public:
    using pqueue = priority_queue<int, std::vector<int>, std::greater<int>>;
    int findSecondMinimumValue(TreeNode* root) {
        //priority_queue<int, std::vector<int>, std::greater<int> > res;
        pqueue res;
        findSecondMiniValueCore(root, root->val, res);
        cout<<res.size()<<endl;
        int len=res.size();
        /*for(int i=0; i<len; i++){
            cout<<res.top()<<" ";
            res.pop();
        }*/
        if (res.size()>0 && res.top()>root->val)
            return res.top();
        else
            return -1;
    }
    void findSecondMiniValueCore(TreeNode* root, int root_value, pqueue &res){
        if(root!=NULL && root->val > root_value) res.push(root->val);
        if(root->left!=NULL) findSecondMiniValueCore(root->left, root_value, res);
        if(root->right!=NULL) findSecondMiniValueCore(root->right, root_value, res);
        
    }
};
```


