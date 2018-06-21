### 226. Invert Binary Tree
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL || (root->left==NULL && root->right==NULL))
            return root;
        //交换左右子节点
        TreeNode* temp=root->left;
        root->left=root->right;
        root->right=temp;
        
        //子树进行递归
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
```
### 234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

```
//把链表分成两个子链表， 然后把其中一个逆转，在一一比较两个链表对应位置元素相等
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        //do with special case;
        if(head==NULL || head->next==NULL)
            return true;
        int len=0;
        ListNode * pcur=head;
        while(pcur){
            len+=1;
            pcur=pcur->next;
        }
        ListNode *lHead=head, *lend=head, *rHead=NULL;
        if(len%2==0){ //偶数个节点
            int half=len/2;
            rHead=head;
            while(half>0){
                lend=rHead;
                rHead=rHead->next;
                half--;
            }
        }
        else{ //奇数个数
            int half=len/2;
            rHead=head;
            while(half>0){
                lend=rHead;
                rHead=rHead->next;
                half--;
            }
            rHead=rHead->next;
        }
        lend->next=NULL;
        //分成两个链表，左子链表lHead~lend, 右子链表rHead~最后一个几点
        //逆转左子链表
        ListNode * lNewHead=inverse(lHead);
        lHead=lNewHead;
        while(lHead && rHead){
            cout<<"lval="<<lHead->val<<" rval="<<rHead->val;
            if(lHead->val != rHead->val)
                return false;
            lHead=lHead->next;
            rHead=rHead->next;
        }
        return true;
        
    }
    //逆转链表
    ListNode * inverse(ListNode* root){
        if(root==NULL || root->next==NULL)
            return root;
        ListNode * head=NULL;
        ListNode * Ppre=NULL, *Pcur=root, *Pnext=Pcur->next;
        while(Pcur){
            Pcur->next=Ppre;
            Ppre=Pcur;
            Pcur=Pnext;
            if(Pnext)
                Pnext=Pnext->next;
        }
        head=Ppre;
        return head;
    }
};
```
### 461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

```
//从低位到位，把x和y对应位的数字(0 or 1)取出，然后在比较， 
//用一个模板数分别与x和y按位与， 00001, 0010, 0100, 1000,
class Solution {
public:
    int hammingDistance(int x, int y) {
        long temp=1;
        int count=0;
        int max_v=max(x,y);
        while(temp <= max_v){
            int result=(temp & x)^(temp & y);
            if(result!=0){
                count+=1;
            } 
            temp=temp<<1;
        }
        return count;
    }
};
```
### 437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

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
    int pathSum(TreeNode* root, int sum) {
        int count=0;
        pathSumCore(root, sum, count);
        if(root!=NULL){
            count+=pathSum(root->left, sum); //加上左子树满足的路径数量
            count+=pathSum(root->right, sum); //加上右子树满足的路径数量
        }
        return count;
    }
    void pathSumCore(TreeNode * root, int sum, int & count){
        if(root==NULL)
            return;
        if(root->val==sum){
            count+=1;
        }
        if(root->left){
            pathSumCore(root->left, sum-root->val,count);
        }
        if(root->right){
            pathSumCore(root->right, sum-root->val,count); //该路径包含root节点
        }        
    }
};
```
### 448. Find All Numbers Disappeared in an Array
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
//时间复杂度O(N), 空间复杂度O(1)
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        for(int i=0; i<nums.size(); i++){
            cout<<"i= "<<i<<" nums[i]="<<nums[i]<<" seq: ";
            printVec(nums);
            if(nums[i]!=nums[nums[i]-1]){  //元素nums[i]不在自己对应的位置i-1
                swap(nums[i], nums[nums[i]-1]);
                --i;
            }
        }
        for(int i=0; i<nums.size(); i++){
            if(nums[i]!=i+1)
                res.push_back(i+1);
        }
        return res;
        
    }
    
    void printVec(vector<int> & nums){
        for(int i=0; i<nums.size(); i++)
            cout<<nums[i]<<",";
        cout<<endl;
    }
};
```
### 572. Subtree of Another Tree
 Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself. 
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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        return isSubtreeCore(s, t) || ( s->left!=NULL ? isSubtree(s->left, t):0) || (s->right!=NULL ? isSubtree(s->right, t):0);
    }
    bool isSubtreeCore(TreeNode* s, TreeNode* t){
        if(s==NULL && t==NULL)
            return true;
        if(s==NULL || t==NULL)
            return false;
        bool found=false;
        if(s->val!=t->val)
            return false;
        else{
            if(s->left==NULL && s->right==NULL && t->left==NULL && t->right==NULL) //叶子节点
                return true;
            found = isSubtreeCore(s->left, t->left);
            found=found & isSubtreeCore(s->right, t->right);
            return found;
        }
    }
};
```
 
