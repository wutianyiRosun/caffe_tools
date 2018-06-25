### 617. Merge Two Binary Trees
 
Given two binary trees and imagine that when you put one of them to cover the other, 
some nodes of the two trees are overlapped while the others are not. 
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree. 

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

class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if(t1==NULL && t2==NULL)
            return NULL;
        else if(t2==NULL && t1 )
            return t1;
        else if(t2 && t1==NULL)
            return t2;
        else {
            t1->val= t1->val+ t2->val;
            t1->left= mergeTrees(t1->left, t2->left);
            t1->right= mergeTrees(t1->right, t2->right);
            return t1;
        }
        
    }
 
};
```

### 66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size=digits.size();
        int flag=1; //puls one 
        digits.push_back(0);
        for(int i=size; i>0; i--){
            digits[i]=(digits[i-1]+flag)%10;
            flag=(digits[i-1]+flag)/10; //进位标志
        }
        if(flag==0){
            auto it=digits.begin();
            digits.erase(it);
        }
        else{
            digits[0]=1;
        }
        return digits;
    }
};
```
