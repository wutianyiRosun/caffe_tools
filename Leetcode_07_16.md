### 179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

```
//Solution: 我们首先定义两个数的大小  a, b我们先把二者转换为a_str, b_str, if a_str+b_str>b_str+ a_str成立， 则a>b
//我们把数组按上面的方式排序, 然后按顺序把这些数拼接（转出字符串直接加)
bool srt(int a,int b)  //降序排列
{
    string x=to_string(a);
    string y=to_string(b);
    return (x+y>y+x);
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        
        string res="";
        if(nums.size()==0)
            return res;
        //检查数组是否都是0
        int fg=1;
        for(int i=0;i<nums.size();i++)
            if(nums[i]!=0){ 
                fg=0; 
                break; 
            }
        if(fg==1)  //数组元素都是0， 则返回0
            return "0"; 
        sort(nums.begin(),nums.end(),srt);
        
        for(auto j:nums){
            cout<<j<<",";
            res+=to_string(j);
        }
        
        return res;
    }
};
```
### 190. Reverse Bits
Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
```
//时间复杂度O（1）
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
    }
};

/*
for 8 bit binary number abcdefgh, the process is as follow:
abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
*/
```

### 191. Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011 

Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
```
class Solution {
public:
   /* int hammingWeight(uint32_t n) {
        uint32_t tmp=1;
        int count=0;
        if( (tmp & n)==1)
            count=1;
        for(int i=1; i<32; i++){
            tmp=tmp<<1;
            if( (tmp & n) ==tmp)
                count+=1;
        }
        return count;
        
        
    }
    */
     int hammingWeight(uint32_t n) {
         int count=0;
         while(n){
             count+=1;
             n=n&(n-1);
         }
         return count;
        
    }
};
         
         
```
### 230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Solution: 先中序遍历，得到元素从小到大排列，然后取第k个
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> nums;
        Inorder(root, nums);
        cout<<nums.size()<<endl;
        return nums[k-1];
    }
    void Inorder(TreeNode* root, vector<int> & nums){
        if(root){
            Inorder(root->left, nums);
            nums.push_back(root->val);
            Inorder(root->right, nums);
        }
    }
};
```
### 378. Kth Smallest Element in a Sorted Matrix
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```
//Solution: 利用优先队列，先把矩阵第1列元素存放到优先队列中，对优先队列pop k-1次，则优先队列top()处的元素是第k大元素
//每次pop()一个元素，同时把其右邻居元素压人优先队列当中,如果没有则跳过

struct record{
    int x;
    int y;
    int val;
    record(int tmp_x, int tmp_y, int tmp_val){
        x=tmp_x;
        y=tmp_y;
        val=tmp_val;
    }
};

bool cmp(record & t1, record & t2){
    return t1.val>t2.val; //"<"为从大到小排列，">"为从小到大排列  
}
class Solution {
public:
   
    int kthSmallest(std::vector<std::vector<int>>& matrix, int k) {
         struct record{
            int x;
            int y;
            int val;
            record(int tmp_x, int tmp_y, int tmp_val){
                x=tmp_x;
                y=tmp_y;
                val=tmp_val;
            }
           };

        auto cmp= [](const record & t1, const record & t2){
            return t1.val>t2.val; //"<"为从大到小排列，">"为从小到大排列  
        };
        //std::priority_queue<record, std::vector<record>, decltype(cmp)> pq(cmp);
        priority_queue<record, std::vector<record>, decltype(cmp)> pq(cmp);
        int n=matrix.size();
        for(int i=0; i<n; i++){
            pq.push(record(i,0, matrix[i][0]));
        }
        for(int j=0; j<k-1; j++){  //pop k-1
            auto tmp=pq.top();
            pq.pop();
            if(tmp.y==(n-1)){
                continue;
            }
            pq.push(record(tmp.x, tmp.y+1, matrix[tmp.x][tmp.y+1]));
        }
        return pq.top().val;
    }
};
```
