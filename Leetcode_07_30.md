### 328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
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
    ListNode* oddEvenList(ListNode* head) {
       
        if(head==NULL || head->next==NULL)
            return head;
        ListNode*  even_head=NULL; //偶数头节点， 0,2,4
        ListNode* odd_head=NULL; //奇数节点头 1,3,5
        
        ListNode* P_even=head;
        ListNode* P_odd=head->next;
        ListNode * P_even_next=NULL;
        ListNode * P_odd_next=NULL;
        ListNode * even_cur=NULL;
        ListNode * odd_cur=NULL;
        while(P_even && P_odd){
           
            if(P_odd->next)
                P_even_next=P_odd->next;
            else
                P_even_next=NULL;
            
            if(P_even_next && P_even_next->next)
                P_odd_next=P_even_next->next;
            else
                P_odd_next=NULL;
            
            P_even->next=NULL; //截断
            P_odd->next=NULL;
            if(even_head==NULL && odd_head==NULL){
                even_head=P_even;
                odd_head=P_odd;
                even_cur=even_head;
                odd_cur=odd_head;
            }
            else{
                even_cur->next=P_even;
                odd_cur->next=P_odd;
                even_cur=P_even;
                odd_cur=P_odd;
            }
            P_even=P_even_next;
            P_odd=P_odd_next;
     }
    if(P_even){
        even_cur->next=P_even;
        even_cur=P_even;
    }
    even_cur->next= odd_head;
    return even_head;   
        
    }
};
```
