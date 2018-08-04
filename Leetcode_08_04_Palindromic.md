### 516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
```
//dp:  初始化dp[i][i]=1;
// fixed i, i+1 <= j <s.length()  如果s[i]==s[j], dp[i][j]=dp[i+1][j-1]+2; 否则dp[i][j]= max( dp[i+1][j], dp[i][j-1])
class Solution{
public:
    int longestPalindromeSubseq(string s)
    {
        vector<vector<int>> dp(s.length(),vector<int>(s.length()));
        //dp[i][j]表示字符串i～j下标所构成的子串中最长回文子串的长度～
        //最后我们需要返回的是dp[0][len-1]的值～
        for(int i=s.length()-1;i>=0;i--)
        {
            dp[i][i]=1;
            for(int j=i+1;j<s.length();j++)
            {
                if(s[i]==s[j])
                    dp[i][j]=dp[i+1][j-1]+2;
                else
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
            }
        }
        return dp[0][s.length()-1];
    }
};
```
### 55. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

```
//Solution: 动态规划求解，assume n=s.size(), 我们定义P[n][n], 任意的P[i][j]表示子字符串s[i,,,j]是否回文串，因此原问题等价于求矩阵P中为1的元素， 取max(j-i+1)，即回文子序列S[i,...,j]的长度
//dp方程： P[i][j]= P[i+1][j-1] && s[i]==s[j]
//初始化P[i][i]=1, P[i][i+1]=(s[i]==s[i+1])

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()<=1)
            return s;
        int len=s.size();
        vector< vector<bool> > P(len, vector<bool>(len, 0));
        //初始化P矩阵
        for(int i=0; i<len; i++){
            P[i][i]=1;
            if(i<len-1)
                P[i][i+1]=(s[i]==s[i+1]);
        }
        
        //dp
        for(int i=len-3; i>=0; i--){
            for(int j=i+2; j<len; j++){
                P[i][j]=(P[i+1][j-1] && (s[i]==s[j]) );
            }
        }
        int max_len=1;
        int index1=1;
        for(int i=0; i<len; i++){
            for(int j=i; j<len; j++){
                if( (P[i][j]==1) && (j-i+1>max_len)){
                    max_len=j-i+1;
                    index1=i;
                }
            }
        }
        return s.substr(index1, max_len);     
    }
};
```

### 368. Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
```
//先排序，然后挨个加元素，动态规划
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> res;
        if(nums.size()<=1)
            return nums;
        sort(nums.begin(), nums.end());
        int len=nums.size();
        int dp[len];  //dp[i]表示已元素nums[i]结束的最大可除子集的大小
        int pre[len];  //pre[i]表示最大可出子集中元素nums[i]的前一个元素，便于回溯
        int IDS_len=0;
        int end_index=-1;
        memset(dp,1, sizeof(dp));
        for(int i=0; i<nums.size(); i++){
            pre[i]= -1;
            for(int j=i-1; j>=0; j--){
                if(nums[i] % nums[j] == 0){
                    if(dp[j]+1>dp[i]){
                        dp[i]=dp[j]+1;
                        pre[i]=j;
                    }
                }
            }
            if(dp[i]> IDS_len ){
                IDS_len = dp[i];
                end_index = i;
            }
        }
        while(end_index!=-1){
            res.push_back(nums[end_index]);
            end_index= pre[end_index];
        }
        return res;
    }
};

```
