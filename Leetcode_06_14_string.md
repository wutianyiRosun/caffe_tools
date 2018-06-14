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
