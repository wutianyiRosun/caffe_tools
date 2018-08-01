### 41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
```
//Solution把该数组中值在1,...,N范围内的元素放在其对应的位置,然后找第一个nums[i]!=i+1,返回i+1
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for(int i=0; i<nums.size(); i++){
            if(nums[i]>0 && nums[i]<=nums.size() && nums[i]!=nums[nums[i]-1]){
                swap(nums[i], nums[nums[i]-1]);
                i--;
            }
            
        }
        for(int i=0; i<nums.size(); i++)
            if(nums[i]!=i+1)
                return i+1;
        return nums.size()+1;
        
    }
};
```
