### 141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

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
//Solution1: 利用一个字典来记录visited node;
//Time complexity: O(N), Space complexity: O(N)
/*
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL) //空list
            return false;
        set<ListNode *> ass_set;
        ListNode * pcur=head;
        while(pcur!=NULL){
            if(ass_set.count(pcur)==0){
                ass_set.insert(pcur);
                pcur=pcur->next;
            }  
            else 
                return true;
        }
        return false;
    }
};*/
//solution1的空间复杂度还是比较高，题目限制了空间复杂度。因此我们利用两个指针来，pcur2走的比较快，相对pcur1.
//如果链表中有cycle，则pcur2一定能碰上pcur1.这就好比我们和同学一块去操场跑步，速度快的总能在一定周期碰上速度慢的同学
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL) //空list
            return false;
        ListNode * pcur1=head;
        ListNode * pcur2=head->next;
        while(pcur1!=pcur2){
            if(pcur2==NULL || pcur2->next==NULL)
                return false;
            pcur2=pcur2->next->next;
            pcur1=pcur1->next;
        }
        return true;
    }
};
```
