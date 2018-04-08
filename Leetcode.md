### 92. Reverse Linked List
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''
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
'''
