### 129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

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
//Solution,采用递归方式求解,对于树中任意一个节点pcur，路径（根节点，到cpur父亲节点的数值和为sum)
//如果当前节点为空则直接返回sum
//如果当前节点不为空， 则计算到当前路径的数值和sum=sum*10+pcur->val
//如果当前节点为叶子节点则返回sum, 否则计算到左儿子路径数值和， 右儿子路径数值和， 然后返回二者和
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int sum=0;
        return sumPathCore(root,sum);
    }
    int sumPathCore(TreeNode* root, int sum){
        if(!root)
            return sum;
        int sumL=0, sumR=0;
        sum=10*sum+root->val;
        
        if(root->left==NULL && root->right==NULL)
            return sum;
        if(root->left)
            sumL= sumPathCore(root->left, sum);
        if(root->right)
            sumR= sumPathCore(root->right, sum);
       
        return sumL+sumR;
    }
};
```
