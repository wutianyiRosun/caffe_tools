### 17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res_pre; //这个已处理好的子字符串的组合
        vector<string> res_cur; //保存当前组合， 组合当前遍历的字符digits[i]与res_pre
        if(digits.size()==0)
            return res_pre;
        for(int i=0;i<digits.size();i++){
            int num=digits[i]-'0';
            //tchar.clear();
            vector<char> tchar=int2chars(num);
            res_cur.clear();
            if(res_pre.size()!=0){
                for(int i=0;i<res_pre.size(); i++){
                    for(int j=0;j<tchar.size();j++)
                        res_cur.push_back(res_pre[i]+tchar[j]);
                }
            }else{
                for(int j=0; j<tchar.size(); j++){
                    string st="";
                    st+=tchar[j];
                    res_cur.push_back(st);
                }
                    
            }
            res_pre.clear();
            res_pre.assign(res_cur.begin(), res_cur.end());               
        }
        return res_cur;
    }
    vector<char> int2chars(int num){
        vector<char> tchar;
        if(num<7){
            for(int i=0;i<3;i++)
                tchar.push_back(char(97+(num-2)*3 +i));
        }else if(num==7){
            for(int assic=112; assic<=115; assic++)
                tchar.push_back(char(assic));
        }
        else if(num==8){
            for(int assic=116; assic<=118; assic++)
                tchar.push_back(char(assic));
        }else{
            for(int assic=119; assic<=122; assic++)
                tchar.push_back(char(assic));
        }
        return tchar;
    }
};
```
###  34. Search for a Range
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2, -1);
        if(nums.size()==0)
            return res;
        int start=0;
        int end = nums.size()-1;
        while(start<=end){
            int mid=(start + end)/2;
            if(nums[mid] < target){
                start=mid+1;
            }
            else if(nums[mid] > target){
                end = mid-1;
            }
            else{
                //find target
                int low=mid;
                while(low>=0 && nums[low]==nums[mid]){
                    low--;
                }
                low=low+1;
                int up = mid;
                while(up < nums.size() && nums[up]==nums[mid]){
                    up++;
                }
                up-=1;
                res[0]=low;
                res[1]= up;
                return res;
            }
        }
        return res;
    }
    
};
```

###  46. Permutations               
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```
//Solution: 把序列第一元素与后面所有元素依次交换， 然后把交换后的序列分成两部分， 第一个元素单独做一部分， 后面所有元素的做一部分， 然后递归的对后面这部分元素也
//进行这样的操作，递归下去，直到遇到最后的元素
/*class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if(nums.size()==0)
            return res;
        else if(nums.size()==1){
            vector<int> midres;
            midres.push_back(nums[0]);
            res.push_back(midres);
            return res;
        }
        else{
            for(int i=0; i<nums.size(); i++){
                cout<<"i= "<<i<<endl;
                swap(nums[0], nums[i]);  //交换第0个元素与其他所有元素
                vector<int> temp;
                for(int i=1;i<nums.size();i++){
                    temp.push_back(nums[i]);
                }
                vector<vector<int>> lastSec=permute(temp);
                int m=lastSec.size();
                for(int k=0;k<m;k++){
                    lastSec[k].insert(lastSec[k].begin(), nums[0]);
                    res.push_back(lastSec[k]);
                }
                swap(nums[0], nums[i]);  //交换回去

            }
            return res;
        }
      
    }
};
*/
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums){
        vector<vector<int>> res;
        if(nums.size()==0)
            return res;
        permuteCore(res, nums, 0); 
        return res;
    }
    void permuteCore( vector<vector<int>>& res, vector<int>& nums, int curIndex) {
        if(nums.size()-1==curIndex){
            vector<int> midres;
            for(int i=0;i<nums.size();i++){
                midres.push_back(nums[i]);
            }
            res.push_back(midres);
        }
        else{
            for(int i=curIndex; i<nums.size(); i++){
                swap(nums[curIndex], nums[i]);  //交换首元素与其他所有元素
                permuteCore(res, nums, curIndex+1); //对后面部分的元素递归调用
                swap(nums[curIndex], nums[i]);  //交换回去
            }
        }
      
    }
};
```

### 62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28
```
//动态规划求解
class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m==0 || n==0)
            return 0;
        vector<vector<int>> dp(m, vector<int>(n, 0)); //dp[i][j]表示从出发点到位置(i,j)的路径数量
        //初始化
        for(int j=0;j<n;j++)
            dp[0][j]=1;
        for(int i=0;i<m;i++)
            dp[i][0]=1;
        
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                dp[i][j]=dp[i-1][j]+dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};
```
### 63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m= obstacleGrid.size();  //row
        int n= obstacleGrid[0].size(); //column
        if(m==0 || n== 0)
            return 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        //初始化边界
        int ob_flag=0; //obstacle flag
        for(int i=0; i<m; i++){
            if(obstacleGrid[i][0]==0 && ob_flag==0){
                dp[i][0]=1;
            }else{
                ob_flag=1;
            }
        }
        ob_flag=0; //obstacle flag 
        for(int j=0; j<n; j++){
            if(obstacleGrid[0][j] == 0 && ob_flag==0){
                dp[0][j]=1;
            }else{
                ob_flag=1;
            }
        }
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                if(obstacleGrid[i][j]==0){
                    dp[i][j]=dp[i-1][j]+dp[i][j-1];
                }
                else{
                    dp[i][j]=0;
                }
            }
        }
        return dp[m-1][n-1];
    }
};
```
