### 61. Rotate List
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
```
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
    ListNode* rotateRight(ListNode* head, int k) {
        
        //some case: return the original list
        if(k==0||head==NULL||head->next==NULL)
            return head;
        int len=1;
        ListNode* p1=head;
        while(p1->next!=NULL){// computing the length of the list
            len+=1;
            p1=p1->next;
        }
        k=k%len;
        if(k==0)
            return head;
        ListNode* p2=head;
        ListNode* newhead=head;
        
        while(k>0){
          p2=p2->next;
          k--;
        }
        p1=head;
        while(p2->next!=NULL){
            p2=p2->next;
            p1=p1->next;
        }
        newhead=p1->next; 
        p1->next=NULL;  //converting the partion[head,..,p1] into single list
        p1=head;
        queue<ListNode*> ass_que;
        ass_que.push(p1);
        while(p1->next!=NULL){ //push the partion[head,..,p1] into single list into queue 
            p1=p1->next;
            ass_que.push(p1);
        }
        while(ass_que.empty()==0){
            p2->next=ass_que.front();
            ass_que.pop();
            p2=p2->next;
        }
        return newhead;     
        
        
      }
};
```
### 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/*Solution 1:

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        //do with special case
        if(head==NULL||head->next==NULL)
            return head;
  
        ListNode* p1=head;
        
        queue<ListNode*> ass_que;
        ass_que.push(head);
        while(p1->next!=NULL){
            p1=p1->next;
            if(p1->val!=ass_que.back()->val){
                ass_que.push(p1);       
            }  
        }
        ListNode* newhead;
        newhead=ass_que.front();
        p1=newhead;
        ass_que.pop();
        while(ass_que.empty()==0){
            p1->next=ass_que.front();
            ass_que.pop();
            p1=p1->next; 
        }
        p1->next=NULL;
        return newhead;
    }
};
*/
//solution 2:
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        //do with special case
        if(head==NULL||head->next==NULL)
            return head;
        ListNode* cur_node;
        cur_node=head;
        while(cur_node->next!=NULL){
             if(cur_node->val==cur_node->next->val)
                 cur_node->next=cur_node->next->next;
             else{
                 cur_node=cur_node->next;
             }
             
            
        }
        return head;
      
    }
};
```

### 92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:

Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:

Given m, n satisfy the following condition:

1 ≤ m ≤ n ≤ length of list.

```
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        //do with some sepcial case
        if(m==n||head==NULL||head->next==NULL)
            return head;

        ListNode* ppre=head;
        ListNode* pcur=head;
        ListNode* pre_m=NULL;
        ListNode* pos_n=head;
        ListNode* pnext=NULL;
        //making pointer cur point position m, pre_m points position m-1
        while(m-1>0){
            pre_m=pcur;
            pcur=pcur->next;
            m--;
           
        }
        printf("pcur->val=%d\n",pcur->val);
        /*if(pre_m!=NULL)
            printf("pre_m->val=%d\n",pre_m->val);*/
        // making pointer pre point position n+1, pointer pos_n point position n,
        while(n>0){
            ppre=ppre->next;  //ppre points position m+1, where may be a NULL
            if(n-1>0)
                pos_n=pos_n->next;
            n--;
        }
        /*if(ppre!=NULL)
            printf("ppre->val=%d\n",ppre->val);
        printf("pos_n->val=%d\n",pos_n->val);*/
        if(pre_m!=NULL){ //denote m>1,pre_m=NULL when m=1
            pre_m->next=pos_n; 
            while(pcur->next!=NULL&& pcur!=pos_n){
                pnext=pcur->next;
                pcur->next=ppre;
                ppre=pcur;
                pcur=pnext;
            }
            pcur->next=ppre;  //[m,...,n] last node points pos n-1
            return head;
            
        }
        else{
            ListNode* newhead=NULL;
            newhead=pos_n;
             while(pcur->next!=NULL&& pcur!=pos_n){
                pnext=pcur->next;
                pcur->next=ppre;
                ppre=pcur;
                pcur=pnext;
            }
            pcur->next=ppre;  //[m,...,n] last node points pos n-1
            return newhead;
        }
    
    }
};
```
