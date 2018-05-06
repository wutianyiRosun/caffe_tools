### 147. Insertion Sort List
Sort a linked list using insertion sort.
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//求解思路，我们采用插入排序原理，不同于在数组上面进行。链表上的插入排序复杂些。我们拿到链表中的一个元素，假设前面的元素都排好序了（这部分的最后一个
元素都指向NULL）,这点非常关键，不然会出现循环链表。我们每次把待插入的元素pcur与排好序的那个子链表进行比较。分两种情况，如果当前元素值小于子链表中
//第一个元素，则该元素做为子链表的新表头newhead.第二种情况则是当前元素值大于排好序的子链表的第一个元素，这中情况我们需要把元素pcur插入到子链表中，
//然后插入的位置有两种，(1）中间//任意位置，则把pcur插入到p2与p1之间； (2)插入到子链表的尾部，这种情况需要进行尾部截断处理。
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if(head==NULL||head->next==NULL)
            return head;
        ListNode* newhead=head;  //排好序链表的头节点 
        ListNode *pcur=head->next;
        int len=1;
        ListNode* pcurPre=head;
        newhead->next=NULL;  //让排好序的元素尾部截断，避免形成循环链表
        while(pcur!=NULL){ 
            len=len+1;
            ListNode *pcurNext=pcur->next; //下一个需要遍历的元素
            pcur->next=NULL;
            if(pcur->val <= newhead->val){//当前元素值小于链表排好序部分的第一个元素值，则把当前元素插在最前面
                ListNode* temp=newhead;
                newhead=pcur;
                newhead->next=temp;
            }else{ //当前元素大于前面排好序部分的第一个元素
                ListNode* p1= newhead;
                ListNode* p2= newhead; //p2用于记录当前元素插入的位置(接折p2后面)
                while(p1!=NULL && (pcur->val > p1->val) ){ //把pcur指向的元素与排好序的所有元素比较，找到插入位置, 
                    p2=p1;
                    p1=p1->next;
                }
                if(p1==NULL){  //当前元素大于前面所有排好序的元素,则当前元素插在排好序的最后面，即p2后面
                    p2->next=pcur;
                    p2->next->next=NULL; //尾部需要截断
                } 
                else{ //当前元素大于前面所有排好序的部分元素， 则插在中间
                     p2->next=pcur;
                     p2->next->next=p1; //pcur插在p2与p1之间
                }
            } 
            pcur=pcurNext;
        }
        return newhead;
        
    }
};
```

55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
             
```
//递归实现
/*
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int end=nums.size();
        return canJumpCore(nums, 0, end-1);
    }
    bool canJumpCore(vector<int>& nums, int start, int end){
        int cur=start;
        int maxStep=nums[cur];
        if(maxStep>=end-start){
            return true;
        }
        else
        {
            if(maxStep==0)
                return false;
            bool res=0;
            for(int i=1;i<=maxStep;i++){
                res=res||canJumpCore(nums, cur+i, end);
                if (res==1)
                    return true;
            }
            return res;
        }
    }
};*/

//贪心算法求解，我们从最右边开始遍历数组，找出当前子数组（cur, last)能够到达last的最靠左边的元素,记为pleft,原问题就等价与pleft==0是否成立
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len=nums.size();
        int pleft=len-1;//开始时，pleft指向最右边的元素, 其index=len-1
        for(int i=len-2;i>=0;i--){
            if(i+nums[i]>=pleft){ //判断当前元素是否够得着pleft,够得着，就更新pleft
                pleft=i; 
            }
        }
        return 0==pleft;
    }
    
};
```



