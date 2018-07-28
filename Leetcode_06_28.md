### 239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window.  time the sliding window moves right by one position. Return the max 
sliding window.
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 ```
 class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> max_res;
        deque<int> slidingWin;  //该队列存对应元素的索引
        if(nums.size()==0)
            return max_res;
        for(int i=0;i<k;i++){
            while(slidingWin.size()>0 && nums[i] > nums[slidingWin.back()])
                slidingWin.pop_back();
            slidingWin.push_back(i); //存储元素值大的索引
        }
        for(int i=k; i<nums.size(); i++){
            max_res.push_back( nums[slidingWin.front()]);
            //cout<<"i="<<i<<" current val="<<nums[i]<<"   slidingWin.size()= "<<slidingWin.size()<<endl;
            //printDeque(slidingWin);
            //slidingWin保存区间 [i-k+1, i] ,k个元素的最大值
            while(slidingWin.size()>0 && nums[i]>=nums[slidingWin.back()])  //当前元素大于队列sildingWin后面一部分元素
                slidingWin.pop_back();
            if(slidingWin.size()>0 && slidingWin.front() <= i-k) //队列的首元素已经滑出滑动窗口了
                slidingWin.pop_front();
            //cout<<"after op, slidingWin.size()= "<<slidingWin.size()<<endl;
            //printDeque(slidingWin);
            slidingWin.push_back(i);
             //printDeque(slidingWin);
        }
        max_res.push_back( nums[slidingWin.front()]);
        return max_res;
    }
    void printDeque(deque<int> nums){
        for(auto item: nums)
            cout<<item<<",";
        cout<<endl;
    }
};
```
### 416. Partition Equal Subset Sum
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

//Solution: 考虑先给数组排序，对于每一个元素，我们选或者不选两种可能，递归下去
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        if(nums.size()<=1)
            return false;
        int sum=0;
        for(int i=0; i<nums.size(); i++){
            sum+= nums[i];
        }
        if(sum%2 !=0)
            return false;
        sum=sum/2;
        int size= nums.size();
        sort(nums.rbegin(),nums.rend());
        return helper(nums, 0, sum);
    }
    bool helper(vector<int> & nums, int index, int  sum){
        if(nums[index]==sum || sum==0)
            return true;
        if(sum<0 || index>nums.size()-1 || sum<nums[index])
            return false;
        return helper(nums, index+1,  sum-nums[index]) || helper(nums, index+1, sum);
    }
};

```
### 581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sor
```
//Solution1: 先复制整个数组，然后排序，再找第一个不匹配的元素与最后一个不匹配的元素
//时间复杂度O(NlogN)
/*
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if(nums.size()<=1)
            return 0;
        vector<int> nums_copy;
        nums_copy.assign(nums.begin(), nums.end());
        sort(nums_copy.begin(), nums_copy.end());
        int left=0;
        int index=0;
        while(index<nums.size() && nums[index]== nums_copy[index]){
            index++;
        }
        left=index;
        if(left==nums.size()) //完全匹配
            return 0;
        int right=nums.size()-1;
        index=nums.size()-1;
        while(index>=0 &&nums[index]== nums_copy[index]){
            index--;
        }
        right=index;
        return right-left+1;
    }
};
*/
//Solution2: 时间复杂度O(N), 空间复杂度O(N)
//我们只需找出无序子数左右边界即可，首先我们从头开始遍历数组，用一个stack来保存我们最开始的上升子序列，当我们碰到一个下降趋势的元素
//即a[i]>a[i+1],此时我们需要确定a[i+1]的正确位置，即与栈中元素进行比较，找到合适的位置k,这样我们遍历整个数组，求出最小的k即为无序
//子数组的左边界，同理找到右边界
class Solution{
public:
    int findUnsortedSubarray(vector<int>& nums) {
        if(nums.size()<=1)
            return 0;
        int left=INT_MAX;
        stack<int> ass_stack;
        for(int i=0; i<nums.size(); i++){
           while(ass_stack.size()>0 && nums[ass_stack.top()]>nums[i]){
               left=min(left, ass_stack.top());
               ass_stack.pop();
               
            }
            ass_stack.push(i);
        }
        while(ass_stack.size()>0)
            ass_stack.pop();
        
        int right=0;
        for(int i=nums.size()-1; i>=0; i--){
            while(ass_stack.size()>0 && nums[ass_stack.top()]<nums[i]){
                right= max(right, ass_stack.top());
                ass_stack.pop();
            }
            ass_stack.push(i);
        }
        return left== INT_MAX? 0: right-left+1;
    }
};
```
### 538. Convert BST to Greater Tree
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

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
    int sum=0;
    TreeNode* convertBST(TreeNode* root) {
        if(root==NULL)
            return root;
        convertBST(root->right);
        sum+=root->val;
        root->val=sum;
        convertBST(root->left);
        return root;
    }
};
```
