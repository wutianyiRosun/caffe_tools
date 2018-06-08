### 33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

```
//pseudo-code
//二分查找法
//对于这样的序列， letf~mid, mid~right,中必有一个为升序列，这样分两种情况，然后在每种情况里，根据nums[mid]，nums[left]与target大小关系，确定区间端点

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int res=-1;
        if(nums.size()==0)
            return res;
        int left=0, right=nums.size()-1;
        while(left <= right){
            int mid= (left + right )/2;
            if(nums[left] <= nums[mid]){  // left ~ mid is ascending order
                if(nums[mid] == target){
                    res=mid;
                    break;
                }
                else if (nums[mid] > target && nums[left]<= target){  // find at left ~ mid 
                    right= mid-1;  
                }
                else{
                    left = mid+1;
                }
            }
            else{   // mid ~ right is ascending order
                if(nums[mid] == target){
                    res=mid;
                    break;
                }else if( nums[mid]< target && target<= nums[right] ){// find at mid ~ right
                    left= mid+1;
                }
                else{
                    right = mid-1;
                }
            }
                         
        }
        return res;
    }
};
```
### 81. Search in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

```
//Solution:
//二分查找， 这个题右重复元素，因此在判断左子序列和右子序列，是否是递增子序列之前需要判断， left, mid, right,
//三个元素是否相等，因为这三者相等的情况下无法判断左右子序列的性质
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        bool res=false;
        if(nums.size()==0)
            return res;
        int left=0, right=nums.size()-1;
        while(left <= right ){
            int mid= (left + right)/2;
            if(nums[mid]==target){
                res=true;
                break;
            }
            else{
                if(nums[mid]==nums[left] && nums[mid]==nums[right]){
                    res =OrderFind(nums, left, right, target);
                    return res;
                }
                if( nums[left] <= nums[mid] ){  //left ~ mid is ascending order
                    if(nums[left]<= target && target < nums[mid]){  //find left ~ mid
                        right = mid -1;
                    }else{
                        left = mid +1;
                    }
                }
                else if(nums[mid] <= nums[right]){ // mid ~ right is scending order
                    if (nums[mid]<target && target<=nums[right]){  //find mid ~ right
                        left= mid +1;
                    }else{
                        right = mid -1;
                    }
                }
            }
        }
        return res;
    }
    bool OrderFind(vector<int> & nums, int start, int end, int target){
        for(int i= start;i<= end;i++){
            if(nums[i]==target)
                return true;
        }
        return false;
    }
};
```
