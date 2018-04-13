今天两道题64，72都是动态规划的题，这类题的套路递归分析，建立子问题与原问题解的关联，然后循环实现，一般情况都得初始化table or 变量。
64: middle level  72: hard level

### 64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.

```
//递归方式
/*
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        if(m==0)
            return 0;
        int n=grid[0].size();  
        int res=minPathSumCore(grid,m-1,n-1);
        return res;
   
    }
    int minPathSumCore(vector<vector<int>>& grid,int m, int n){
        if(m==0){
            int sum=0;
            for(int i=0;i<=n;i++)
                sum+=grid[0][i];
            return sum;
        }
        if(n==0){
            int sum=0;
            for(int i=0;i<=m;i++)
                sum+=grid[i][0];
            return sum;
        }
        int res01=minPathSumCore(grid,m-1,n)+grid[m][n];
        int res10=minPathSumCore(grid,m,n-1)+grid[m][n];
        //int res00=minPathSumCore(grid,m-1,n-1)+grid[m][n];  //允许斜着走的情况
        return min(res01,res10);
    }
};*/
//循环的方式
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        if(m==0)
            return 0;
        
        int n=grid[0].size(); 
        if(m==1){
            int sum=0;
            for(int i=0;i<grid[0].size();i++)
                sum+=grid[0][i];
            return sum;
        }  
        int sum[m][n];
        //inital table
        for(int i=0;i<m;i++){
            if(i==0)
                sum[0][0]=grid[0][0];
            else
                sum[i][0]=sum[i-1][0]+grid[i][0];
        }
        for(int i=0;i<n;i++){
            if(i==0)
                sum[0][0]=grid[0][0];
            else
                sum[0][i]=sum[0][i-1]+grid[0][i];
        } 
        for(int i=1;i<m;i++)
            for(int j=1;j<n;j++){
                int temp1=sum[i-1][j]+grid[i][j];
                int temp2=sum[i][j-1]+grid[i][j];
                sum[i][j]=min(temp1,temp2);
            }       
        return sum[m-1][n-1];
    }
};
```

### 72. Edit Distance
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

```
//动态规划，递归分析，循环实现
//Time complexity: O(MN), Space complexity: O(MN)

class Solution { 
public:
    int minDistance(string word1, string word2) { 
        int m = word1.length(), n = word2.length();
        vector<vector<int> > OPT(m + 1, vector<int> (n + 1, 0));
        for (int i = 1; i <= m; i++)
            OPT[i][0] = i;
        for (int j = 1; j <= n; j++)
            OPT[0][j] = j;  
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) 
                    OPT[i][j] = OPT[i - 1][j - 1];
                else {
                    int insert= OPT[i][j - 1] + 1;
                    int deletee= OPT[i-1][j] + 1;
                    int replace= OPT[i-1][j - 1] + 1;
                    OPT[i][j] = min(replace, min(insert,deletee));
                }
            }
        }
        return OPT[m][n];
    }
};
```
