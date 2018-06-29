### 543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root. 
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
//Solution： 对于1颗树， 这个最长直径如果经过根节点
//也可能不经过该根节点， 经过其左儿子节点或者右儿子节点
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(root==NULL)
            return 0;
        int depth=computeMaxDepth(root->left)+computeMaxDepth(root->right);
        int left_depth = diameterOfBinaryTree(root->left);
        int right_depth = diameterOfBinaryTree(root->right);
        return max(max(depth, left_depth), right_depth);
    }
    int computeMaxDepth(TreeNode* root){
        if(root==NULL)
            return 0;
        
        int left_h=computeMaxDepth(root->left);
        int right_h= computeMaxDepth(root->right);
        return left_h>right_h ? left_h+1:right_h+1;
    }
};
```
### 337. House Robber III

 The thief has found himself a new place for his thievery again. There is only one entrance to this area, 
 called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart
 thief realized that "all houses in this place forms a binary tree". It will automatically contact the police 
 if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.

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
class Solution {
public:
    int rob(TreeNode* root) {
        if(root==NULL)
            return 0;
        //根节点偷
        int money_1= root->val;
        if(root->left)
            money_1+=rob(root->left->right)+rob(root->left->left);
        if(root->right)
            money_1+=rob(root->right->left)+rob(root->right->right);
        //根节点不偷
        int money_2 =0;
        if(root->left)
            money_2+= rob(root->left);
        if(root->right)
            money_2+= rob(root->right);
        return max(money_1, money_2);
        
    }
};*/

//深度优先搜索求解
class Solution{
public:
    int rob(TreeNode* root){
        return dfs(root, false);
    }
    int dfs(TreeNode* root, bool flag){
        if(root==NULL)
            return 0;
        if(!flag){
            //前者代表根节点偷， 后者代表根节点不偷
            return max(root->val+dfs(root->left, true)+dfs(root->right, true), dfs(root->left, false)+dfs(root->right, false) );
        }
        if(flag) //flag为真，当前根节点不能偷
            return  dfs(root->left, false)+dfs(root->right, false);
    }
};
```


### 338. Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2]. 
```
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res(num+1,0);
        if(num==0){
            return res;
#        }
        res[0]=0;  //val=0
        res[1]=1;  //val=1
        res[2]=1;
        int nearest=2;
        for(int i=3; i<=num; i++){
            nearest= powerOf2(i)? i: nearest;
            res[i]= res[i-nearest]+1;
        }
        return res;
    }
    bool powerOf2(int n){ //n是否为2的指数次方

return (n&(n-1))==0;
    }
};
```
### 124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \

2   3

Output: 6
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
` *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res=INT_MIN;
        maxPathSumCore(root, res);
        return res;
    }
`    int maxPathSumCore(TreeNode* root, int& res){
        if(root==NULL)
            return 0;
        int left=maxPathSumCore(root->left, res);
        int right=maxPathSumCore(root->right, res);
        if(left<0) left=0;
        if(right<0) right=0;
        if(left+right+root->val > res)
            res=left+right+root->val;
        return root->val+max(right, left);
    }
};
```
### 128. Longest Consecutive Sequence


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.
Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


```
//我们先把数组全部放入到unordered_set中，然后遍历数组元素nums[i]，找以nums[i]元素开始的连续子序列，并统计其长度
//时间复杂度，O(nlogn)，空间复杂度O(N)
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        unordered_set<int> nums_set;
        for(int i=0; i<nums.size(); i++)
            nums_set.insert(nums[i]);
        int res_length=1, current_length=1;
        int currentNum=0;
        for(int i=0; i<nums.size(); i++){
            if(nums_set.find(nums[i]-1)==nums_set.end()){
                currentNum=nums[i]+1;
                current_length=1;
                while(nums_set.find(currentNum)!=nums_set.end()){
                    current_length++;
                    currentNum++;
                }
                res_length=max(current_length, res_length );
            }
        }
        return res_length;
    }
};
```
