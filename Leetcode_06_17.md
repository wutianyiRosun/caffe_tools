### 287. Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

```
//采用二分查找的思想， 对于某个区间[start, end]，我们计算两个子区间[start, mid], [mid+1, end] 对应区域内数
//字在整个数组中出现的个数， 如果[start, mid]区间统计的数字个数大于该区间长度， 则重复数字出现在这个区间， 
//否则， 重复的数字出现在[mid+1, end]区间时间复杂度, 循环进行Log(n)次， 然后每次需要O(n)时间统计数量， O(nlogn),空间复杂度O(1)
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int start=1;
        int end=nums.size()-1;
        //Binary search
        while(start<=end){
            int mid= (start + end)/2;
            int leftNum= CountRange(nums, start, mid); //computing the numbers of [start, mid]
            if(start==mid && leftNum>1){
                return start;
            }
            //int RightNum= CountRange(nums, mid+1, end);
            if(leftNum>mid-start+1){
                //左子区间内数字出现次数大于该区间长度，则重复数字出现在该区间范围
                end= mid;
            }
            else{  //否则重复数字出现在右区间范围
                start=mid+1;           
            }
        }
    }
    
    int CountRange(vector<int>& nums, int start, int end){
        int res=0;
        for(int i=0; i<nums.size(); i++){
            if(start<=nums[i] && nums[i]<=end){
                res+=1;
            }
        }
        return res;
    }
};
```
### 136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res=nums[0];
        for(int i=1; i<nums.size(); i++){
            res=res^nums[i]; //异火，所有相同的两个数异或之后都为0，然后0与那个出现一次的数异或的结果就是这个出现1次的数
        }
        return res;
    }
};
```
### 137. Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3

Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
```
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones=0, twos=0;
        for(int i=0;i<nums.size();i++){
            ones=(ones^nums[i])&~twos;
            twos=(twos^nums[i])&~ones;
        }
        return ones;
    }
};
```
###    260. Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

```
//Solution: 我们知道对于一个数组，只有一个数出现一次，其他数都出现两次，我们可以对序列所有元素进行异或运算，就可以找到这个
//只出现一次的数。  现在我们面对的是有两个各出现一次的数。 我们把他们分到两个组， 每个组只包含一个只出现一次的数。 对于如何将x 和 y
//分到两组， 我们根据x和y的二进制最低的不同位进行分组，也就是二者异或后最第的“1”位  
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> result;
        //first, computing res=x^y
        int res=nums[0];
        for(int i=1; i<nums.size(); i++){
            res=res^nums[i];
        }
        //finding the lowest "1" bit
        int flag=0x01;
        while(true){
            if(flag&res) break;
            flag=flag<<1;
        }
        int num1=0, num2=0;
        //dividing two groups according to  the lowers "1" bit of res 
        for(auto num: nums){
            if(num & flag){
                num1^=num;
            }
            else{
                num2^=num;
            }
        }
        result.push_back(num1);
        result.push_back(num2);
        return result;
    }
};
```
### 300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```
//Solution1: 时间复杂度O(N^2)
//用dp[i]表示以元素nums[i]结束的最长子序列， 然后对于dp[i+1], 我们需要考虑所有j, 0<=j<i+1, 比较nums[j]与nums[i]
//如果nums[i]>nums[j]&& dp[j]+1>dp[i],则dp[i]=dp[j]+1
/*
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int len=nums.size();
        vector<int> dp(len,0);
        dp[0]=1;
        int maxLen=1;
        for(int i=1; i<nums.size(); i++){
            dp[i]=1;
            for(int j=0; j<i; j++){
                if(nums[i]>nums[j] && dp[j]+1>dp[i]){
                    dp[i]=dp[j]+1;
                }
                   
            }
            if(dp[i]>maxLen)
                maxLen=dp[i];
        }
        return maxLen;
    }
};*/

//Solution2,我们先找出一个与该最长递增子序列等长度的序列，  我们建立一个vector<int> res;
//遍历nums,对于nums[i], if(nums[i]<res[0])则res[0]=nums[i]
//if(nums[i]>res[res.size()-1]), 则res.push_back(nums[i])
//if(num[i]>dp[k]&& num[i]<dp[k+1]) 则dp[k+1]=nums[i]
//时间复杂度O(nlogn)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        int len=nums.size();
        vector<int> dp;
        dp.push_back(nums[0]);
        for(int i=1; i<nums.size(); i++){
            auto it = lower_bound(dp.begin(), dp.end(), nums[i]);
            if(it == dp.end()){
                dp.push_back(nums[i]);
            }
            else{
                *it = nums[i];
            }
        }
        return dp.size();
    }
};
```
