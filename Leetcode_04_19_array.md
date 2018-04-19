### 167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

```
//更快的一种解决方式是先用二分法确定target在有序数组中的位置，
//然后在改位置左半部分子数组用如下方式查找
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        if(numbers.size()>=2){
            vector<int> res;
            int preIndex=0;
            int backIndex=numbers.size()-1;
            while(preIndex<backIndex){
                int tempSum=numbers[preIndex]+numbers[backIndex];
                if(tempSum==target){  
                    res.push_back(preIndex+1);
                    res.push_back(backIndex+1);
                    return res;
                }
                else if(tempSum>target){  //如果当前和大于target,向左移动第二个数backIndex
                    backIndex--;
                }else{        //如果当前和小于target,则向右移动第一个数backIndex
                    preIndex++;
                }
            }
            
        }  
    }
};
```


### 189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II

```
//Solution: 通过例子发现旋转数组规律：
//（1）先整体逆序整个数组，然后把该数组分为左右两个子数组（以index=k-1为分界点），最后分别逆序两个子数组

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k=k%nums.size();
        int first_start=0, first_end=nums.size()-1;
        int left_start=0, left_end=k-1;
        int right_start=k, right_end=first_end;
        InverseArray(nums, first_start, first_end);  //原数组逆序
        InverseArray(nums, left_start, left_end);   //左子数组逆序
        InverseArray(nums, right_start, right_end);  //右子数组逆序
        
    }
    void InverseArray(vector<int>& nums, int start, int end){
        for(int i=start;i<end;i++){
            int temp=nums[i];
            nums[i]=nums[end];
            nums[end]=temp;
            end--;
        }
    }
};
```
