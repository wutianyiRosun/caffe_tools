### 718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        if(A.size()==0 || B.size()==0)
            return 0;
        int lenA=A.size();
        int lenB=B.size();
        //int  dp[lenA][lenB]; //dp[i][j]表示A中以A[i]元素结束B中以B[j]元素结束的最长公共子序列,原问题等价于max(dp)
        vector<vector<int>> dp(lenA , vector<int>(lenB, 0) );
        int max= dp[0][0];
        for(int i=0;i<lenA;i++)
            for(int j=0;j<lenB;j++){
                if(A[i]==B[j]){
                    if(j>0 && i>0){
                        dp[i][j]=dp[i-1][j-1]+1;
                    }
                    else
                        dp[i][j]=1;
                }
                else
                    dp[i][j]=0;
                if(dp[i][j]>max)
                    max= dp[i][j];
            }
        return max;
    }
};
```
