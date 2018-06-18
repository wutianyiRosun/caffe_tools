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
