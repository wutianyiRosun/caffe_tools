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

### 456. 132 Pattern
 Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:

Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0]

```
//Solution1: O(n^3)枚举 me Limit Exceeded]
/*
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if(nums.size()<3)
            return 0;
        for(int i=0; i<nums.size()-2; i++){
            for(int j=i+1; j<nums.size()-1; j++){
                if(nums[j]>nums[i]){
                    for(int k=j+1; k<nums.size(); k++){
                        if(nums[i]<nums[k] && nums[k]<nums[j])
                            return true;
                    }
                }
            }
        }
        return false;
    }
};*/
//Solution 2: 我们定义一个数组min[n], min[i]保存序列nums[0,...,i]中最小的元素, 然后我们开一个stack,我们从数组尾部往前遍历， 如果stack为空，则把元素压人stack中，如果stack不为空且当前元素小于stack顶的元素， 则将当前元素压人stack中,如果当前元素大于stack顶元素，则将stack顶的元素pop出来， 知道
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if(nums.size()<3)
            return 0;
        int len= nums.size();
        int mins[len];
        mins[0]=nums[0];
        for(int i=1; i<len; i++){
            mins[i]=min(mins[i-1], nums[i]);
        }
        stack<int> numsk_stack;
        for(int i=len-1; i>=0; i--){
            if(nums[i]>mins[i]){
                while(numsk_stack.size()>0 && numsk_stack.top()<=mins[i] )  //如果当前栈顶元素小于mins[i]， pop
                    numsk_stack.pop();
                if(numsk_stack.size()>0 && numsk_stack.top()< nums[i]) // mins[i]<numsk_stack.top()< nums[i]
                    return true;
                numsk_stack.push(nums[i]);
            }
        }
        return false;
    }
};

```
