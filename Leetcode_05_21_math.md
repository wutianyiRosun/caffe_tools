### 413. Arithmetic Slices

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.

1, 1, 2, 5, 7


A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

```
//动态规划求解，假设OPT[i]表示子数组A[0,...,i-1]的arithmetic slices数量，该子数组长度len=i
//我们再看OPT[i+1]
//case 1: 如果A[i+1]-A[i]==diff, diff为任意两个连续元素之差
//我们看增加的arithmetic slices情况，长度为3的增加一个，长度为4的增加一个，长度为len的增加一个，然后再增加了一个长度为len+1的
//即总共增加的个数为len-3+1+1 = len-1,所以OPT[i+1]=OPT[i]+len-1,此处len为A[i]的长度
//case 2: 如果A[i+1]-A[i]!=diff,则重新开始统计Arithmetic slices,同时记录新diff
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        if (A.size()<3)
            return 0;
        int diff=A[1]-A[0];
        int len=2;
        int numAS=0;
        for(int j=2; j<A.size() ;j++){
            if(A[j]-A[j-1]==diff){
                if(len==2){
                    numAS+=1;
                    len++;
                }
                else{
                    numAS+=len-1;  //OPT[i+1]=OPT[i]+len-1
                    len=len+1;
                } 
            }else{
                diff=A[j]-A[j-1];
                len=2; //重新开始统计了
            }
        }
        return numAS;
    }
};
```

### 523. Continuous Subarray Sum
 Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

```
//我们采用增量法求解，我们假设当前子序列A[0, i-1]没有保护符合要求的子序列，长度len1=i，
//对于子序列A[0, i],其长度len2=i+1
//我们做如下考虑，其在A[0, i-1]的基础上新增加的子序列有如下情况：
//长度为len2=i+1的增加一种， 其和为sum(A[0,i-1])+A[i]
//长度为len1=i的增加一种， 其和为sum(A[1,i-1])+A[i]
//...
//长度为j的增加一种， 其和为sum(A[i-j+1,i-1])+A[i]
//长度为2的增加一种， 其和为A[i-1]+A[i]
//用vector<int> sum表示当前序列A[0,...,i]的各种长度子序列和,sum[i]表示i个数的和
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int len=nums.size();
        if(len<2)
            return 0;
        vector<int> sum(len+1,0);
        sum[2]=nums[0]+nums[1]; //sum[1]表示两个数之和
        if( (k!=0 && sum[2]%k==0 )|| (sum[2]==0&& k==0))
            return true;
        else{
            for(int j=2;j<len;j++){
                for(int index=j;index>1;index--){
                    sum[index+1]=sum[index]+nums[j]; //sum[index]表示index数之和
                    if( (k!=0 && sum[index+1]%k==0) || (sum[index+1]==0&& k==0))
                        return true;
                }
                sum[2]=nums[j]+nums[j-1];
                if( (k!=0 && sum[2]%k==0) || (sum[2]==0&& k==0))
                    return true;
            }
        }
        return false;
    }
};
```
