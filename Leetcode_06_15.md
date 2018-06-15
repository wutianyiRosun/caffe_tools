### 206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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
    ListNode* reverseList(ListNode* head) {
        //do with case empty list or single-node list
        if(head==NULL || head->next== NULL)
            return head;
        ListNode *Ppre=NULL;
        ListNode *Pcur=head;
        ListNode * Pnext=Pcur->next;
        ListNode * newhead=NULL;
        while(Pcur!=NULL){
            Pcur->next=Ppre;
            Ppre=Pcur;
            Pcur=Pnext;
            if(Pnext!=NULL) //当pcur指向最后一个节点时， Pnext此时已经指向了NULL节点
                Pnext=Pnext->next;
        }
        newhead= Ppre;
        return newhead;
    }
};
```
