### 154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

```
//Solution: case1: 这个数组就是排好序的数组，即nums[0]<nums[len-1]； case2: 数组以中间某个元素进行旋转， 
//考虑到数组中存在重复的元素，我们采用二分法查找，如果遇到pleft == pmid == pright,我们则顺序查找最小的元素
//case3: 只有一个元素，直接返回该元素
class Solution {
public:
    int findMin(vector<int>& nums) {
        int len=nums.size();
        if(len==1)
            return nums[0];
        cout<<nums[0]<<" "<<nums[len-1]<<endl;
        if(nums[0]<nums[len-1])
            return nums[0];
        int pleft=0;
        int pright=len-1;
        
        while(pleft<pright){
            int pmid=(pleft+pright)/2;
            
            if(pright-pleft==1)
                return nums[pright];
            //左边子数组递增，则最小值在右边子数组
            if(nums[pleft]<=nums[pmid]  && nums[pmid]>nums[pright]){
                pleft=pmid;
            }
            //右边子数组递增，最小值在左子数组
            if( nums[pright]>=nums[pmid] && nums[pleft]>nums[pmid] ){
                pright=pmid;
            }
            if(nums[pleft]==nums[pmid] && nums[pright]==nums[pmid]){
                return simpleFindMin(nums, pleft, pright);
            }
        }
    }
    
    int simpleFindMin(vector<int> & nums, int pleft, int pright){
        int min=nums[pleft];
        for(int i=pleft+1; i<= pright; i++){
            if(nums[i]<min)
                min=nums[i];
        }
        return min;
    }
};
```
### 496. Next Greater Element I
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

```
//Solution: 本题主要考察vector查找元素位置find(nums.begin(), nums.end(), val);和计算绝对距离index = distance(nums.begin(), pindex)的应用
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> result;
        int fsize=findNums.size();
        int tsize=nums.size();
        for(int i=0; i<fsize; i++){
            int val= findNums[i];
            auto pindex= find(nums.begin(), nums.end(), val);
            if(pindex!=nums.end()){
                int index = distance(nums.begin(), pindex);
                bool find_flag=0;
                while(index<=tsize-1){
                    if(nums[index]>val){
                        result.push_back(nums[index]);
                        find_flag=1;
                        break;
                    }
                    index+=1;
                }
                if(!find_flag)
                    result.push_back(-1);
                
            }else{
                result.push_back(-1);
            }
        }
        return result;
    }
};
```

### 503. Next Greater Element II

 Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

```
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int size= nums.size();
        vector<int> result;
        if(size==1){
            result.push_back(-1);
            return result;
        }
        for(int i=0; i<size; i++){ //数组后半部分
            bool find_flag=0;
            for(int j=i+1; j<size; j++){
                if(nums[j] > nums[i]){
                    find_flag=1;
                    result.push_back(nums[j]);
                    break;
                }
            }
            if(!find_flag){
                for(int k=0;k<=i;k++){  //后半部分为找到，则再取前半部分查找
                     if(nums[k] > nums[i]){
                         find_flag=1;
                         result.push_back(nums[k]);
                         break;
                     }
                }
            }
            if(!find_flag)
                result.push_back(-1);
        }
        return result;
    }
};
```


