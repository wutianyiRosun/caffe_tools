### 494. Target Sum
 You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int start=0;
        int end=nums.size()-1;
        int ways=0;
        findTargetSumWaysCore(nums, start, end, S, ways);
        return ways;
    }
    void findTargetSumWaysCore(vector<int>& nums, int start, int end, int target, int &ways){
        if (start==end){
            if(target==0 && nums[end]==0){
                ways+=2;
            }
            else if(target==nums[end] || target==(-1)*nums[end]){
                ways+=1;
            }
        }
        else{
            findTargetSumWaysCore(nums, start+1, end, target+nums[start], ways);
            findTargetSumWaysCore(nums, start+1, end, target-nums[start], ways);
        }
    }
};
```
### 560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
```
//定义数组dp[], dp[i]表示子序列nums[0,..,i]之和
//对于以元素nums[j]结束的连续子序列，我们计算dp[j]-dp[i]==k, i=0,1,...,j-1,等号成立表示子序列nums[i+1,...,j]之和是k

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if(nums.size()==0)
            return 0;
        int len=nums.size();
        int dp[len]; //dp[i]表示子序列nums[0,..,i]之和
        dp[0]=nums[0];
        for(int i=1;i<len;i++){
            dp[i]=dp[i-1]+nums[i];
        }
        int count=0;
        for(int j=0;j<len;j++){
            for(int i=j-1; i>=0; i--){
                if(dp[j]-dp[i]==k)  //nums[i+1,...,j]
                    count+=1;
            }
            if(dp[j] == k)
                count+=1;
        }
        return count;
    }
};
```
### 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1
```
//二分查找,时间复杂度log(n)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size=nums.size();
        if(target<=nums[0])  //比最小的还小
            return 0;
        if(target>nums[size-1])//比最大的还大
            return size;
        int start=0, end=size-1;
        while(start<=end){
            int mid= (start+end)/2;
            if(nums[mid]>=target && nums[mid-1]<target){  //则在区间【start, mid]  找出第一个大于等于target的数字nums[mid], return mid
                return mid;
            }
            else if (nums[mid]>target ){
                end=mid-1;
            }
            else{
                start = mid+1;
            }
        }
    }
};
```
