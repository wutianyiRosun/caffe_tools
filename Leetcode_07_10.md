### 91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


```
//动态规划求解: dp[i】表示子字符串s[0...i]的译码方式，那么对于dp[i+1]的译码方式情况如下：
//case 1: if（s[i]*10+s[i+1]>26, dp[i+1]=dp[i]
//case 2: if(s[i]*10+s[i+1]<=26 dp[i+1]=dp[i]+1
//other case: dp[i+1]=0
class Solution {
public:
    int numDecodings(string s) {
        if (s.size() == 0 || s[0] == '0')
            return 0;
        vector<int>dp(s.size() + 1);  //dp(i)表示s[0]到s[i-1]这一共i个字符组成的子串编码个数
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 1; i < s.size(); i++)
        {
            int tmp = (int)atoi(s.substr(i - 1, 2).c_str());
            if (tmp <= 26 && tmp >= 10)  //s[i-1]与s[i]结合译码
                dp[i + 1] += dp[i - 1]; //dp[i+1] 序列s[0]到s[i]的译码方式, dp[i-1]表示序列s[0]都s[i-2]的译码方式
            if (tmp%10 != 0)//s[i]！=0  s[i]还能单独译码
                dp[i + 1] += dp[i];
        }
        return dp[s.size()];
    }
};
    
```
