### 228. Summary Ranges
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```
//O(n)时间 O(1)空间
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if(nums.size()==0)
            return res;
        int start=nums[0];
        int cur=nums[0];
        for(int i=1; i<nums.size(); i++){
            if(nums[i]==cur+1){
                cur=nums[i];
                
            }
            else{  //nums[i]>cur+1
                if(cur==start){
                    res.push_back(to_string(start));
                }
                else{
                    res.push_back(to_string(start)+"->"+to_string(cur));
                }
                start=nums[i];
                cur=nums[i];
            }
        }
        if(cur==start){
            res.push_back(to_string(start));
        }
        else{
            res.push_back(to_string(start)+"->"+to_string(cur));
        }

        
        return res;
    }
};
```
### 873. Length of Longest Fibonacci Subsequence

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].

```
//dp[i][j]表示子序列A[i]到A[j]中最长F序列长度
//k<i<j, dp[i][j]= dp[k][i]+1, if(A[k]+A[i]==A[j])
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        int n = A.size();
        unordered_map<int, int> m; 
        for (int i = 0; i < n; i++) m[A[i]] = i;
        vector<vector<int>> dp(n, vector<int>(n, 2));
        int ans = 0;
    	for (int j = 1; j < n; j++)
    		for (int i = 0; i < j; i++)
    			if (m.find(A[j]-A[i]) != m.end() && m[A[j] - A[i]] < i){  //A[k]=A[j]-A[i],保持k<i<j
    				dp[i][j] = max(dp[i][j], dp[m[A[j] - A[i]]][i] + 1);
                    ans = max(ans, dp[i][j]);
                }
    	return (ans==2)?0:ans;
    }
};
```
