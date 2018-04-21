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

### 414. Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
```
//Solution: 一开始看到这个题我们可以马上想到的一个方法就是先排序,然后从右往左寻找第三大值, Time complexity: O(nlogn).
//但由于题目限制时间复杂为O(N).因此这个解法不符合要求.容易想到用三个变量保存first, second, third max value; 遍历数组,每次按要求去更新这三个最值
//时间复杂度: O(N),空间复杂度: O(1)

class Solution {
public:
        int thirdMax(vector<int>& nums) {
        int firstmax=nums[0], secondmax=0, thirdmax=0;
        bool secflag=0, thirdflag=0; //record second max and third max is NULL or not.
        for(int cur =0; cur< nums.size(); cur++){
            //更新第一大值
            //if (cur>0 && nums[cur-1]==nums[cur]) continue; //跳过相同元素
            、
            if(nums[cur]>firstmax){
                if(secflag==0){
                    secondmax=firstmax; 
                    firstmax=nums[cur];
                    secflag=1;
                }
                else{ //(secondmax!=NULL )
                    thirdmax=secondmax;
                    thirdflag=1;
                    secondmax=firstmax;
                    firstmax=nums[cur];
                    
                }
            }
               
            //更新第二大值情况是 当前值小于firstmax,并且大于secondmax,或者是第二最大值为空的情况
            if(nums[cur]<firstmax && ( (secflag==1 && nums[cur]>secondmax) || secflag==0 )  ){
                if(secflag==0){ //第二大值为空
                    secondmax=nums[cur];
                    secflag=1;
                    
                }
                else{ //第二大值不为空
                    thirdmax=secondmax;
                    thirdflag=1;
                    secondmax=nums[cur];
                }
                
            }
                
            //更新第三大值情况是 当前第二值不为空,且当前值小于第二大值, 然后第三大值小于当前值或者第三大值为空的情况
            if(secflag!=0 && nums[cur]<secondmax  && ( (thirdflag!=NULL && nums[cur]>thirdmax) || thirdflag==NULL) ){
                thirdflag=1;
                thirdmax=nums[cur];
            }
    
            //printf("cur= %d, max1= %d max2= %d max3= %d secflag=%d thirdflag=%d \n", cur, firstmax, secondmax, thirdmax, secflag, thirdflag);
        }
        if(thirdflag!=NULL)
            return thirdmax;
        return firstmax;
        
    }
};
```

### 153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
```
//二分查找法, Time Complexity: O(logN)
class Solution {
public:
    int findMin(vector<int>& nums) {
        int len=nums.size();
        int start=0, end = len-1;
        int middle=(start+end)/2;
        if(nums[0]<nums[len-1])//排序数组
            return nums[0];
        while(start<end && middle>start){
            
           
            if(nums[middle]>nums[start]){ //左子数组递增,最小值在右边子数组
                start=middle;
            } 
            if(nums[middle]< nums[end]){  //右子数组递增, 最小值在左边子数组
                end=middle;
            }
            middle=(start+end)/2;
        }
        return nums[start]>nums[end]?nums[end]:nums[start];
    }
};
```



