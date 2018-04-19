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
