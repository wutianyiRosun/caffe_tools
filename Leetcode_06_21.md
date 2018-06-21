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
