### 31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```
//字典序： 对于一个全排列， P=P1P2,...Pn, 其下一个排列， 从排列的右端开始找，找出第一个数字， 这个数字比它右边的数字小（即从右端开始升序的边界)
//记为P[j], 然后从P[j+1~n]子序列中找出大于P[j]的元素中最小的那个记为P[k], j+1<=k<=n,交换二者的位置, //然后升序排列子序列nums[j+1~end]
//如果找不到P[j],这当前排列是最后一个排列了,则顺序排列整个序列

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size()<=1)
            return;
        int j=-1;
        int size=nums.size();
        for(int i=size-2; i>=0; i--){ //寻找nums[j], 从右端开始的升序序列的边界，升序序列不包括nums[j]
            if(nums[i]< nums[i+1]){
                j=i;
                break;
            }
        }
        int k=j+1;
        if(j!=-1){
            //在子序列nums[j+1, size-1]中找出那些大于nums[j]的元素中最小的那个, nums[k]  
            for(int t=j+1;t<=size-1; t++){
                if(nums[t]>nums[j])
                    k=t;            
            }
            //swap nums[k] and nums[j]
            int temp= nums[k];
            nums[k]=nums[j];
            nums[j]=temp;
            sort(nums.begin()+j+1, nums.end());
        }
        else{
            //交换整个序列，得到最小的排列
            sort(nums.begin(), nums.end());
        }
    }
};

```
### 98. Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    2
   / \
  1   3
Output: true
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
//Solution1: 先中序遍历，然后判断中序遍历是否为递增数组，
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(root==NULL)
            return true;
        vector<TreeNode*> nums;
        Inorder(root, nums);
        for(int i=1;i<nums.size();i++){
            if(nums[i]->val <= nums[i-1]->val)
                return false;
        }
        return true;
    }
    void Inorder(TreeNode* root, vector<TreeNode*> &nums){
        if(root->left!=NULL)
            Inorder(root->left, nums);
        nums.push_back(root);
        if(root->right!=NULL)
            Inorder(root->right, nums);
    }
    
};
```
### 114. Flatten Binary Tree to Linked List
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

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
//递归解决， 对于根节点，我们先把左子树整成链表， 根节点的右指针指向左子树的根节点， 然后把指针移动到左子树的最后一个节点， 让其指向右子书整成的链表的表头，如此递//归下去
class Solution {
public:
    void flatten(TreeNode* root) {
       flattenCore(root);
    }
    TreeNode* flattenCore(TreeNode* root){
        if(root==NULL || (root->left==NULL && root->right==NULL))
            return root;
        TreeNode* leftsubTree=root->left;
        TreeNode* rightsubTree=root->right;
        root->left=NULL;
        root->right= flattenCore(leftsubTree);
        TreeNode* pcur=root;
        while(pcur->right!=NULL){
            pcur=pcur->right;
        }
        pcur->right= flattenCore(rightsubTree);
        return root;
    }
};
```
### 200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
```
//Solution: grid, 消灭连续的1， 统计消灭的次数，即岛屿的数量
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        for(int i=0;i<grid.size();i++){
            for(int j=0;j<grid[i].size(); j++){
                if(grid[i][j]=='1'){
                    count+=1;
                    propagation(grid, i,j);
                }
                
            }
        }
        return count;
    }
    void propagation( vector<vector<char>>& grid, int i, int j){
        int m=grid.size();
        int n= grid[0].size();
        if(grid[i][j]=='1'){
            grid[i][j]='0';
            if(i>0){ //up
                propagation(grid, i-1,j);
            }
            if(i<m-1){ //down
                propagation(grid, i+1,j);
            }
            if(j>0){ //left
                propagation(grid, i, j-1);
            }
            if(j<n-1){ //right
                propagation(grid,i,j+1);
            }
        }
    }
};
```
