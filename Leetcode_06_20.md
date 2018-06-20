### 31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```
//字典序： 对于一个全排列， P=P1P2,...Pn, 其下一个排列， 从排列的右端开始找，找出第一个数字， 这个数字比它右边的数字小（即从右端开始升序的边界)
//记为P[j], 然后从P[j+1~n]子序列中找出大于P[j]的元素中最小的那个记为P[k], j+1<=k<=n,交换二者的位置, //然后升序排列子序列nums[j+1~end]
//如果找不到P[j],这当前排列是最后一个排列了,则顺序排列整个序列

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        if(nums.size()<=1)
            return;
        int j=-1;
        int size=nums.size();
        for(int i=size-2; i>=0; i--){ //寻找nums[j], 从右端开始的升序序列的边界，升序序列不包括nums[j]
            if(nums[i]< nums[i+1]){
                j=i;
                break;
            }
        }
        int k=j+1;
        if(j!=-1){
            //在子序列nums[j+1, size-1]中找出那些大于nums[j]的元素中最小的那个, nums[k]  
            for(int t=j+1;t<=size-1; t++){
                if(nums[t]>nums[j])
                    k=t;            
            }
            //swap nums[k] and nums[j]
            int temp= nums[k];
            nums[k]=nums[j];
            nums[j]=temp;
            sort(nums.begin()+j+1, nums.end());
        }
        else{
            //交换整个序列，得到最小的排列
            sort(nums.begin(), nums.end());
        }
    }
};

```
