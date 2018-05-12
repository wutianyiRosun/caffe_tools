154. Find Minimum in Rotated Sorted Array II

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
``
