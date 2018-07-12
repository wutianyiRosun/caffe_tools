### 5. Longest Palindromic Substring
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
        int n=s.size();
        vector<vector<bool>> P(n, vector<bool>(n, 0));
        //初始化
        for(int i=0; i<n; i++){
            P[i][i]=true;
            if(i<n-1)
                P[i][i+1]=(s[i]==s[i+1]);
        }
        
        for(int i=n-3; i>=0; i--){
            for(int j=i+2; j<n; j++){
                P[i][j]= ( P[i+1][j-1]&&(s[i]==s[j]));
            }
        }
        int max=1, index_i=0, index_j=0;
        for(int i=0;i<n; i++){
            for(int j=i+1; j<n; j++){
                if(P[i][j]==1 && (j-i+1)>max){
                    index_i=i;
                    index_j=j;
                    max= j-i+1;
                }
            }
        }
        cout<<index_i<<", "<<index_j<<endl;
        return s.substr(index_i, index_j-index_i+1);
          
    }
};
```

### 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```
//我们先遍历第一个字符串的所有字符， 然后比较其余所有字符串该位置的字符是否与这个字符相等
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
        string ret;
        for(int i = 0; i < strs[0].length() ; ++i)
        {
            //for(size_t j = 0; j < strs.size() - 1; ++j)
            for(int j = 0; j < strs.size() - 1; ++j)
            {   
                if(strs[j][i] != strs[j+1][i])
                    return ret;
            }
            ret += strs[0][i];
        } 
        return  ret;
    }
};
```
