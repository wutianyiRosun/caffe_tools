### 69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             
```
//二分法求解
class Solution {
public:
    int mySqrt(int x) {
        int ans;
        if(x==0) return 0;
        int start=1, end=x;
        while(start<=end){
            int mid=(start+end)/2;
            if(mid<=x/mid){
                start=mid+1;
                ans=mid;
            }
            else{
                end=mid-1;
            }
        }
        return ans;
        
    }
};

```

### 73. Set Matrix Zeroes
Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```
//Solution1:  空间复杂度O(mn),我们用另外一个mask数组记录原始矩阵中出现0的位置，然后根据mask矩阵元素mask[i][j]==0 ,则把原矩阵中第i行和第j列设置为0
//Solution2: 空间复杂度O(m+n)， 我们用两个数组长度分别为m和n来记录原始矩阵中哪些行包含0元素，哪些列包含0元素
//Solution3: 我们用两个变量记录第0行和第0列是否包含有0元素，然后再遍历矩阵中的元素，对于a[i][j],如果a[i][j==0, 则把该元素对应的a[i][0]和a[0][j]置为0
//然后在根据a[i][0]是否为0把第i行所有元素置为0,a[0][j]是否为0把第j列元素置为0， 最后根据一开始的两个变量是否把第0列本身和第0行本身的元素全置为0
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        bool zeroRow=false, zeroCol=false;
        for(int i=0; i<m; i++){
            if(matrix[i][0]==0){
                zeroCol=true;
                break;
            }
        }
        for(int j=0; j<n; j++){
            if(matrix[0][j]==0){
                zeroRow=true;
                break;
            }
        }
        
        for(int i=0; i<m; i++){
            for(int j=0;j<n; j++){
                if(matrix[i][j]==0){
                    matrix[0][j]=0;  //对应到第0行元素
                    matrix[i][0]=0;  //对应到第0列元素
                }
            }
        }
        //check 第0行元素中那些元素为0，把为0的元素所在的列置为0
        for(int j=1;j<n; j++){
            if(matrix[0][j]==0){
                for(int i=1; i<m;i++){
                    matrix[i][j]=0;
                }
            }
        }
        //check 第0列中元素中那些元素为0，把为0的元素所在的行置为0
        for(int i=1;i<m; i++){
            if(matrix[i][0]==0){
                for(int j=1; j<n;j++){
                    matrix[i][j]=0;
                }
            }
        }
        if(zeroRow){ //原始矩阵中第0行包含0元素，则第0行所有元素置0
            for(int j=0; j<n; j++){
                matrix[0][j]=0;
            }
        }
        if(zeroCol){ //原始矩阵中第0列包含0元素，则第0行所有元素置0
            for(int i=0; i<m; i++){
                matrix[i][0]=0;
            }
        }
    }
};
```

