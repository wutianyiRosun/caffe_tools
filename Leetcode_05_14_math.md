### 223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

###
```
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        
        int area1 = abs(A-C) * abs(B-D);
        int area2 = abs(E-G) * abs(F-H);
        int x1=0,x2=0; //重合小矩形的左下角、右上角横坐标
        if(C<=G && E<=C){
            x2 = C;
            x1 = max(A,E);
        }else if(C>G&& A<G){
            x1 = max(A,E);
            x2 = G;
        }
        else{
            x1=x2=0;
        }
        int y1=0, y2=0; //重合小矩形的左下角、右上角的纵坐标
        if(H<=D && H>B){
            y2= H;
            y1 = max(B, F);
        }else if(H>D && F<D){
            y2=D;
            y1=max(B, F);
        }else{
            y1=y2=0;
        }
        int commonArea =abs(y2-y1)* abs(x2-x1);
        return area1+area2-commonArea;
        
    }
};
```

### 160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* common=NULL;
        if(headA==NULL || headB==NULL)
            return common;
        int lenA=0;
        ListNode * pcur=headA;
        while(pcur){
            lenA++;
            pcur=pcur->next;
        }
        int lenB =0;
        pcur = headB;
        while(pcur){
            lenB++;
            pcur=pcur->next;
        }
        ListNode *pcurA=headA;
        ListNode *pcurB=headB;
        if(lenA>lenB){
            int i= lenA-lenB;
            while(i>0){
                pcurA=pcurA->next;
                i--;
            }
        }
        if(lenA<lenB){
            int i= lenB-lenA;
            while(i>0){
                pcurB=pcurB->next;
                i--;
            }
        }
        cout<<lenA<<" "<<lenB<<endl;
        while(pcurB!=NULL && pcurA!=NULL && pcurB != pcurA ){
            pcurB=pcurB->next;
            pcurA=pcurA->next;
        }
        if(pcurB!=NULL && pcurB==pcurA)
            return pcurA;
        else
            return common;
        
    }
};
```
