### 142. Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

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
    ListNode *detectCycle(ListNode *head) {
        //do with empty list or single-node list
        ListNode * begin=NULL;
        if(head==NULL)
            return begin;
        
        //using two points P1 and P2 to find the cycle begin, the Speed of P1 is faster than P2
       
        ListNode * P2= head;
        ListNode * P1= head->next;
        if(P1==NULL)
            return begin;
        
        while(P1!=NULL && P1!=P2){  //P1==P2相遇，break while
            P2=P2->next;
            if(P1->next!=NULL){
                P1=P1->next->next;
            }
            else{  //the faster pointer P1 arrives at NULL node, no cycle
                return begin;
            }
            
        }
        if(P1==NULL)
            return begin;
        
        //computing the length of cycle after finding a node in cycle
        int CycleLen=1;
        P2=P2->next;
        while(P2!=P1){
            CycleLen+=1;
            P2=P2->next;
        }
        
        //init P1=head P2=head+len, first meeting position is cycle begin
        P1=head;
        P2=head;
        while(CycleLen>0){
            P2=P2->next;
            CycleLen--;
        }
        while(P1!=P2){  //meeting at the cycle begin
            P1=P1->next;
            P2=P2->next;
        }
        begin=P1;
        return P1;
    }
};
```

### 148. Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//using merge sort's spirits, first dividing long list into two short list, and recursively ,  finally merge them
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        //do with empty or single node list
        if(head==NULL || head->next==NULL)
            return head;
        //computing the length of list
        int len=0;
        ListNode * pcur=head;
        while(pcur!=NULL){
            len+=1;
            pcur=pcur->next;
        }
        ListNode * newHead = mergeSort(head, len);
        return newHead;
    }
    ListNode * mergeSort(ListNode* head, int len){
        if(len==1)
            return head;
        int pos=len/2-1; //divide bounder 0~pos-1,  pos~len
        ListNode * head1= head; //head node of left section
        ListNode * head2= NULL;  //head node of right section
        int k=0;
        while(k<pos){
            head1=head1->next;
            k++;
        }
        head2=head1->next;
        head1->next=NULL; //divide list into two lists
        head1=head;
        
        ListNode *p= mergeSort(head1, pos+1);
        ListNode *q= mergeSort(head2, len-pos-1);
        
        //merge two lists into one list
        
        ListNode *resHead =NULL;
        ListNode *resCur =NULL;
        while(p!=NULL && q!=NULL){
            if(p->val <= q->val){
                if(resHead==NULL){
                    resHead=p;
                    resCur=p;
                }
                else{
                    resCur->next=p;
                    resCur=resCur->next;
                }
                p=p->next;
            }
            else if(p->val > q->val){
                if(resHead == NULL){
                    resHead=q;
                    resCur=q;
                }
                else{
                    resCur->next=q;
                    resCur=resCur->next;
                }
                q=q->next;
            }
           
        }
        if(p!=NULL)
            resCur->next=p;
        if(q!=NULL)
            resCur->next=q;
        return resHead;
    }
};
```
