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
//动态规划求解: dp[i】表示子字符串s[0...i]的译码方式，

//other case: dp[i+1]=0
class Solution {
public:
    int numDecodings(string s) {
        if (s.size() == 0 || s[0] == '0')
            return 0;
        vector<int>dp(s.size(), 0);  //dp(i)表示s[0]到s[i]这一共i个字符组成的子串编码个数
        dp[0] = 1; //字符0的编码个数
        dp[1] = 0;
        int tmp = (int)atoi(s.substr(0, 2).c_str());
        if(tmp<=26 && tmp>=10)
            dp[1]=1;
        if(tmp%10!=0)
            dp[1]+=1;
        
        for (int i = 2; i < s.size(); i++)
        {
            int tmp = (int)atoi(s.substr(i - 1, 2).c_str());
            if (tmp <= 26 && tmp >= 10)  //s[i-1]与s[i]结合译码
                dp[i] += dp[i-2]; //dp[i+1] 序列s[0]到s[i]的译码方式, dp[i-1]表示序列s[0]都s[i-2]的译码方式
            if (tmp%10 != 0)//s[i]！=0  s[i]还能单独译码
                dp[i] += dp[i-1];
        }
        return dp[s.size()-1];
    }
};
    
```

### 130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

```
//Solution: 我们首先从board的边界开始，对于边界上的元素'O'，我们将与该元素相链接的'O'元素都标记为 '1'.然后子遍历board矩阵中为'1'的元素替换成'O',
//为'0'的元素替换成'X'
class Solution {
public:
    void propagation(vector<vector<char>> & board, int i, int j){
        int m=board.size();
        int n= board[0].size();
        if(board[i][j]!='O')
            return ;
        if(board[i][j]=='O'){  //board[i][j]=='O'
            board[i][j]='1';
            if(i>0)
                propagation(board, i-1, j);
            if(i<m-1)
                propagation(board, i+1, j);
            if(j>0)
                propagation(board, i, j-1);
            if(j<n-1)
                propagation(board, i, j+1);
            
        }
    }
    void solve(vector<vector<char>>& board) {
        int m=board.size();
        if(m==0)
            return;
        int n= board[0].size();
        if(n==0)
            return;
        //第一行和最后一行做propagation
        for(int j=0; j<n; j++){
            if(board[0][j]=='O'){
                //board[0][j]='1';
                propagation(board, 0, j);
            }
            if(board[m-1][j]=='O'){
                //board[m-1][j]='1';
                propagation(board, m-1, j);
            }
        }
        //第一列和最后一列
        for(int i=0; i<m; i++){
            if(board[i][0]=='O'){
                //board[i][0]='1';
                propagation(board, i, 0);
            }
            if(board[i][n-1]=='O'){
                //board[i][n-1]='1';
                propagation(board, i, n-1);
            }
        }
        
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j]=='O'){
                    board[i][j]='X';
                }
                if(board[i][j]=='1'){
                    board[i][j]='O';
                }
                
            }
        }
        
    }
};
```
### 162. Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
```
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if(nums.size()==1)
            return 0;
        for(int i=0; i<nums.size(); i++){
            if(i>0){
                if(nums[i]>nums[i-1] ){
                    if(i+1<nums.size()){
                        if(nums[i]>nums[i+1])
                            return i;
                    }
                    else{
                        return i;
                    }
                }
            }
            else{ //i==0
                if(i+1<nums.size()){
                    if(nums[i]>nums[i+1])
                            return i;
                }
                
            }
        }
    }
};
```
