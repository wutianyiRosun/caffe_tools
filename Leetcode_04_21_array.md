### 18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

```
//Solution: 先给数组按从小到达的顺序排列.设想一下把这个题目简单化,假如只考虑两个数之和,我们定义两个指针
//一个指向最左端,一个指向最右端,再计算二者之和, 1)如果小于target,则右移左指针, 2)如果大于target则左移右指针,
//3)如果等于target,则满足要求.两个数之和我们好处理.现在问题是4个数, 自然想到如何利用2个数的思路来解决这个问题
//自然想到先去计算两个数的和,然后余下两个数用之前的方法去寻找

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        //check input
        vector <vector<int>> res;
        if(nums.size()<4)
            return res;
        // sort nums, form small to big
        sort(nums.begin(), nums.end());
        int len=nums.size();
        printf("nums[0]=%d\tnums[n-1]=%d\n",nums[0], nums[len-1]);
       
        int curIndex=0; //当前元素index
        for(curIndex=0; curIndex<len-3; curIndex++){
            //printf("curIndex=%d\n", curIndex);
            if(curIndex>0 && nums[curIndex-1] == nums[curIndex]) continue;//secIndex==curIndex时会执行下面的循环体,后期跳过相同的元素
            if(nums[curIndex] + nums[curIndex+1] + nums[curIndex+2] + nums[curIndex+3] > target) break; 
            //最小的和都大于target退出整个循环
            if(nums[curIndex] + nums[len-3] + nums[len-2] + nums[len-1] < target) continue; 
            //当前元素与最大三个元素之和, 即最大的和都小于target,退出本次循环
            
            for(int secIndex=curIndex+1; secIndex<len-2; secIndex++){
                //printf("cur Index=%d   secIndex=%d\n", curIndex, secIndex);
                if (secIndex>curIndex+1 && nums[secIndex-1] == nums[secIndex]) continue; //secIndex==curIndex时会执行下面的循环体,后期跳过相同的元素
                
                if(nums[curIndex] + nums[secIndex] + nums[secIndex+1] + nums[secIndex+2] > target) break; 
                //最小的和都大于target退出整个循环
                
                if(nums[curIndex] + nums[secIndex] + nums[len-2] + nums[len-1] < target) continue; 
                //当前元素与最大三个元素之和, 即最大的和都小于target,退出本次循环
    
                
                int fTwoSum=nums[curIndex]+nums[secIndex];
              
                //用2Sum的方法寻找剩下的两个数
                int threeIndex=secIndex+1;
                int fourIndex=len-1;

                while(threeIndex < fourIndex){
                    int FourSum=fTwoSum+nums[threeIndex]+nums[fourIndex]; //4Sum
                    if(FourSum < target)
                        threeIndex++;
                    else if(FourSum > target)
                        fourIndex--;
                    else{
                        res.push_back(vector<int>{nums[curIndex], nums[secIndex], nums[threeIndex], nums[fourIndex]});
                        printf("index= %d  %d %d %d \n", curIndex, secIndex, threeIndex, fourIndex);
                        
                        while(nums[threeIndex+1] == nums[threeIndex] && threeIndex<fourIndex)
                            threeIndex+=1;  //跳过相同的元素
                        threeIndex+=1;
                        while(nums[fourIndex-1] == nums[fourIndex]  && threeIndex<fourIndex)
                            fourIndex-=1;
                        fourIndex-=1;
                       
                        /*
                        do{threeIndex++;}while(nums[threeIndex]==nums[threeIndex-1] && threeIndex<fourIndex);  
                        //do while先执行循环体,再判断,循环体至少执行一次
                        do{fourIndex--;}while(nums[fourIndex]==nums[fourIndex+1] && threeIndex<fourIndex);
                        */
                        
                    } //  FourSum == target
                }   
                
            }
        }
        return res;
    }
};
```
