### 718. Maximum Length of Repeated Subarray
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        if(A.size()==0 || B.size()==0)
            return 0;
        int lenA=A.size();
        int lenB=B.size();
        //int  dp[lenA][lenB]; //dp[i][j]表示A中以A[i]元素结束B中以B[j]元素结束的最长公共子序列,原问题等价于max(dp)
        vector<vector<int>> dp(lenA , vector<int>(lenB, 0) );
        int max= dp[0][0];
        for(int i=0;i<lenA;i++)
            for(int j=0;j<lenB;j++){
                if(A[i]==B[j]){
                    if(j>0 && i>0){
                        dp[i][j]=dp[i-1][j-1]+1;
                    }
                    else
                        dp[i][j]=1;
                }
                else
                    dp[i][j]=0;
                if(dp[i][j]>max)
                    max= dp[i][j];
            }
        return max;
    }
};
```

### 96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```
//递归实现
/*class Solution {
public:
    int numTrees(int n) {
        return numTreesCore(1, n);
    }
    int numTreesCore(int a, int b){
        if(a>=b)
            return 1;
        else if(b-a==1)
            return 2;
        else{
            int sum=0;
            for(int k=a; k<=b; k++)
                sum+=numTreesCore(a, k-1)*numTreesCore(k+1, b);
            return sum;                
        }
    }
};*/
//循环实现
//DP, 从1～n中选取根节点i, (i=1,2,...,n),则小于i的元素作为左子树， 对应序列[1,i-1],  大于i的元素作为右子树，对应序列【i+1, n]，
// G(n)= f(1,n)+f(2,n)+...+f(n,n),  此处f(i, n)表示以元素i为根节点的BST的数量
//容易知道f(i, n)= G(i-1)*G(n-i), G(0)=1, G(1)=1
//G(i)=f(1,i)+f(2,i)+...+f(i,i)
class Solution {
public:
    int numTrees(int n) {
       vector<int> G(n+1, 0);
        G[0]=1;
        G[1]=1;
        for(int i=2; i<=n;i++){
            //computing G(i)
            for(int k=1;k<=i;k++){
                G[i] += G[k-1]*G[i-k]; //G(i)=f(1,i)+f(2,i)+...+f(i,i)
            }
        }
        return G[n];
    }
};
```

### 241. Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10


```
//递归实现
/*
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> result;
        int len=input.size();
        for(int i=0; i<len; i++){
            char cur=input[i];
            if( cur =='-' || cur =='+' || cur =='*'){
                vector<int> result1 = diffWaysToCompute(input.substr(0,i)); //0~i-1, i个
                vector<int> result2 = diffWaysToCompute(input.substr(i+1));  //i+1~end
                for(auto res1: result1)
                    for(auto res2: result2){
                        if(cur== '-'){
                            result.push_back(res1-res2);
                        }
                        else if(cur=='+'){
                            result.push_back(res1+res2);
                        }
                        else{
                            result.push_back(res1*res2);
                        }
                    }
            }    
        }
        if(result.size()==0){
            result.push_back( atoi(input.c_str()) );
        }
        return result;
    }
};
*/
//带内存记忆,避免计算重复子问题
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        map<string, vector<int>> dpmap;
        return diffWaysToComputeCore(input, dpmap);
    }
    vector<int> diffWaysToComputeCore(string input, map<string, vector<int>>&  dpmap) {
        vector<int> result;
        int len=input.size();
        for(int i=0; i<len; i++){
            char cur=input[i];
            if( cur =='-' || cur =='+' || cur =='*'){
                
                vector<int> result1;  //左子字符串的结果
                string substr1= input.substr(0, i);
                auto it = dpmap.find(substr1);
                if(it != dpmap.end()){
                    result1 = it->second;
                }
                else{
                     result1 = diffWaysToComputeCore(input.substr(0,i), dpmap); //0~i-1, i个
                }
                vector<int> result2; //右子字符串的结果
                string substr2= input.substr(i+1);
                auto it2 = dpmap.find(substr2);
                if(it2!=dpmap.end()){
                    result2= it2->second;
                }
                else{
                    result2 = diffWaysToComputeCore(input.substr(i+1), dpmap);  //i+1~end
                }
                
                for(auto res1: result1)
                    for(auto res2: result2){
                        if(cur== '-'){
                            result.push_back(res1-res2);
                        }
                        else if(cur=='+'){
                            result.push_back(res1+res2);
                        }
                        else{
                            result.push_back(res1*res2);
                        }
                    }
                
            }    
        }
        if(result.size()==0){
            result.push_back( atoi(input.c_str()) );
        }
        dpmap.insert(pair<string, vector<int> >(input, result));
        return result;
    }
};
```
