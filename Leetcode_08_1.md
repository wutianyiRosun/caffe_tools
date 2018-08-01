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
### 74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

```
//时间复杂度Log(M)+log(N)
//首先确定target在哪一行，二分标准判断nums[mid][0]与nums[mid][n-1]与target大小关系
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size();
        if(m==0)
            return false;
        int n=matrix[0].size();
        if(n==0)
            return false;
        int up=0, down=m-1;
        int mid;
        while(up <= down){
            mid= (up + down)/2;
            if(matrix[mid][0]<=target  && target<= matrix[mid][n-1])
                break;
            else if(matrix[mid][0]>target){
                down=mid-1;
            }
            else if(matrix[mid][n-1]<target){
                up= mid+1;
            }
        }
        if(matrix[mid][0]>target || target>matrix[mid][n-1])
            return false;
        //在第mid行进行二分查找
        int left=0, right= n-1;
        while(left<=right){
            int mid1=(left+right)/2;
            if(matrix[mid][mid1]==target)
                return true;
            else if(matrix[mid][mid1]>target){
                right=mid1-1;
            }
            else{
                left=mid1+1;
            }
        }
        return false;
       
        
    }
};
```
### 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```
//dfs
class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int> > res;
        vector<int> combination;
        combinationSum(candidates, target, res, combination, 0);
        return res;
    }
private:
    void combinationSum(vector<int> &candidates, int target, vector<vector<int> > &res, vector<int> &combination, int begin) {
        if (!target) {
            res.push_back(combination);
            return;
        }
        for (int i = begin; i < candidates.size() && target >= candidates[i]; i++) {
            combination.push_back(candidates[i]);
            combinationSum(candidates, target - candidates[i], res, combination, i);
            combination.pop_back();
        }
    }
};
```
