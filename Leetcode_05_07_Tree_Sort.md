### 113. Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

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
//采用循环实现利用前序遍历（先根节点，然后左子节点，最后右子几点),采用前序遍历，如果当前节点不是叶子节点，我们则把它压入一个栈中，同时统计栈中数值之和；
//考虑到要记录路径各个节点，我们在利用一个vector来同步保存数值序列。 如果当前节点为叶子节点： 1)sum+pcur->val==target, 则该节点与栈中保存的所有节
//点构成的路径符合要求, 同时把当前节点的值Push到数值序列， 然后把整个序列放到最后的结果vector中。 2）如果sum+pucr->val!=target, 则我们从栈中取最top的节点，然后把它的右子节点进行入栈。同步记录vector数值序列。最后结束时
//solution 1与solution 2差别在于pathSumCore()函数的singlePath参数传递方式，一个是引用，一个是值传递
//递归实现
/*solution 1
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> allPath;
        vector<int> singlePath;
        pathSumCore(root, sum, singlePath, allPath);
        return allPath;
    }
private:
    void pathSumCore(TreeNode* curnode, int sum, vector<int> & singlePath, vector<vector<int>> & allPath){
        if(curnode==NULL) return ;
        singlePath.push_back(curnode->val);
        if(curnode->left==NULL && curnode->right==NULL && curnode->val==sum )
            allPath.push_back(singlePath);
        pathSumCore(curnode->left, sum - curnode->val, singlePath, allPath);
        pathSumCore(curnode->right, sum - curnode->val, singlePath, allPath);
        cout<<"curNode="<<curnode->val<<" singlePath.size= "<<singlePath.size()<<endl;
        singlePath.pop_back();
        
    }
};*/
//solution 2
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> allPath;
        vector<int> singlePath;
        pathSumCore(root, sum, singlePath, allPath);
        return allPath;
    }
private:
    void pathSumCore(TreeNode* curnode, int sum, vector<int> singlePath, vector<vector<int>> & allPath){ 
        if(curnode==NULL) return ;
        singlePath.push_back(curnode->val);
        if(curnode->left==NULL && curnode->right==NULL && curnode->val==sum ){
            allPath.push_back(singlePath);
            cout<<"find path"<<"end point="<<curnode->val<<endl;
        } 
        pathSumCore(curnode->left, sum - curnode->val, singlePath, allPath);  
        pathSumCore(curnode->right, sum - curnode->val, singlePath, allPath);
        cout<<"curNode="<<curnode->val<<" singlePath.size= "<<singlePath.size()<<endl;
        //singlePath.pop_back();
        
    }
};
```

### 169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

```
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int len=nums.size();
        sort(nums.begin(), nums.end());
        int index=len/2;
        return nums[index];
    }
};
```

