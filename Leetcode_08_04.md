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
