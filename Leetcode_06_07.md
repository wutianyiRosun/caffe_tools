### 307. Range Sum Query - Mutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```
/* Solution1:
class NumArray {
private:
    vector<int> data;
public:
    NumArray(vector<int> nums) {
       data=vector<int>(nums.size(),0);
       for(int i=0;i<nums.size();i++)
           data[i]=nums[i];
    }
    void update(int i, int val) {
        data[i]=val;
    }
    int sumRange(int i, int j) {
        int sum=0;
        for(int k=i;k<=j;k++)
            sum+=data[k];
        return sum;
    }
};
*/
//Solution2:
class NumArray {
private:
    vector<int> data;
    vector<int> sum;
public:
    NumArray(vector<int> nums) {
       data=vector<int>(nums.size(),0);
       sum = vector<int>(nums.size(),0);
        
       for(int i=0;i<nums.size();i++){
            data[i]=nums[i];
            if(i==0){
                sum[i]=nums[0];
            }
            else{
                sum[i]=sum[i-1]+nums[i];
            }
            cout<<"i= "<<i<<" "<<"sum[i]="<<sum[i]<<endl;
       }
    }
    void update(int i, int val) {
        int diff =val-data[i];
        data[i]=val;
        for(int k=i;k<sum.size();k++)
            sum[k]=sum[k]+diff;
    }
    int sumRange(int i, int j) {
        return sum[j]-sum[i]+data[i];
    }
};

```
