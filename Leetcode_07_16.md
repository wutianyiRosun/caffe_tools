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
    int hammingWeight(uint32_t n) {
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
