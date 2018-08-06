### 313. Super Ugly Number
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
 
 ```
 //Solution1: 就是枚举1到N中所有的数字，然后判断每个数字是否为UglyNumber
//Solution2: 用空间换时间，假设数组res[i]中已经右排好序的几个UglyNumber，当前最大值为M,那接下来这个UglyNumber
//肯定是前面某一个丑数乘以primes里面的每个元素，取最小的,因此我们可以把primes[i]与结果数组res的所有元素相乘得到第一个大于M的值， 记为M_i, 
//这样我们取所有M_i中的最小的数作为M的下一个丑数。 但这个过程中会有冗余，每次都重复计算了很多小于M的丑数， 因此我们要为每个Primes[i]标记它下一次重哪个丑数开始乘，使得Primes[i]*(* T[i]) >M, 
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        //int * res = new int[n];
        int res[n];
        res[0]=1;
        vector<int*> T(primes.size(), res);
        int nextUglyIndex=1;
        while(nextUglyIndex < n){
            int min_value = min_primes(primes, T);
            res[nextUglyIndex]=min_value;
            for(int i=0; i<T.size(); i++){
                while((*T[i])*primes[i] <= min_value)
                    ++T[i];
            }
            nextUglyIndex++;
        }
        return res[n-1];
    }
    
    int min_primes(vector<int> & primes, vector<int* > & T){
        int res=INT_MAX;
        for(int i=0; i<primes.size(); i++){
            res= min(res, primes[i] * (*T[i]));
        }
        return res;
    }
};
```
### 32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```
//Solution3: 枚举 O(N^3)
//Solution4: 以每个字符为起点， O(N^2)
//Solution1
//动态规划求解， 我们标记数组dp[n], dp[i]表示以s[i]结束的子字符串中LVP最大长度
// dp[i]== dp[i-2]+2;  if( S[i-1]=='(' && S[i]==')' )
// dp[i]== dp[i-1-dp[i-2-dp[i-1]]]+ dp[i-1]+2  if(s[i-1-dp[i-1]== '(' && s[i]==')'])
//O(N)时间复杂度和空间复杂度
/*
class Solution {
public:
    int longestValidParentheses(string s) {
        int n= s.size();
        vector<int > dp(n, 0);
        int max_count=0;
        for(int i=1; i<n; i++){
            if(s[i-1]=='(' && s[i]==')'){
                 dp[i]= i-2>=0 ? dp[i-2]+2 : 2;
            }
            else if( s[i-1-dp[i-1] ]== '(' && s[i]==')'){
                dp[i]= dp[ i-2-dp[i-1] ] + dp[i-1]+2;
            }
            max_count= max( max_count, dp[i]);
               
        }
 
        return max_count;
    }
};
*/
//Solution2: 以左括号为标准，从左向右统计最大长度， 然后以右括号为中心，从右向左统计最大长度
//O(N)时间复杂度 O(1)空间
class Solution{
public:
    int longestValidParentheses(string s){
        int max_len=0;
        int left=0;
        int right=0;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='('){
                left++;
            }
            else {
                right++;
            }
            if(left==right){
                max_len=max( max_len, 2*left);
            }
            else if(right>left){
                left=0;
                right=0;
            }
        }
        left=0, right=0;
        for(int i=s.size()-1; i>=0;  i--){
            if(s[i]=='('){
                left++;
            }
            else {
                right++;
            }
            if(left==right){
                max_len=max( max_len, 2*left);
            }
            else if(left>right){
                left=0;
                right=0;
            }
        }
        return max_len;
    }
    
};

```
