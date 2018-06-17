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
