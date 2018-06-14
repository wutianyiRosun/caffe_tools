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
### 152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
//DP求解
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int len= nums.size();
        if(len==1)
            return nums[0];
        int opt[len][2];  //opt[i][0]表示以nums[i]结束的子数组乘积最小值,opt[i][1]表示以元素nums[i]结束的子数组乘积的最大值,预案为题等价于求max(dp)
        //init opt[0][0]=opt[0][1]=nums[0];
        opt[0][0]=nums[0];
        opt[0][1]=nums[0];
        int maxRes=nums[0];
        cout<<"i=0 "<<" opt[0][0]="<<opt[0][0]<<" opt[0][1]="<<opt[0][1]<<endl;
        for(int i=1; i<len; i++){
            if(nums[i]>0){
                opt[i][0]= min(opt[i-1][0]*nums[i], nums[i]);
                opt[i][1]= max(opt[i-1][1]*nums[i], nums[i]);
            }
            else if(nums[i]<0){
                opt[i][0]= min(opt[i-1][1]*nums[i], nums[i]);
                opt[i][1]= max(opt[i-1][0]*nums[i], nums[i]);
            }
            else{
                opt[i][0]=0;
                opt[i][1]=0;
            }
            cout<<"i= "<<i<<" opt[i][0]="<<opt[i][0]<<" opt[i][1]="<<opt[i][1]<<endl;
            maxRes=max(maxRes, opt[i][0]);
            maxRes=max(maxRes, opt[i][1]);
        }
        return maxRes;
    }
};
```
### 198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

```
//递归实现
/*
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==0)
            return 0;
        if(nums.size()==1)
            return nums[0];
        
        int end=nums.size()-1;
       
       return robCore(nums, end);
    }
    int robCore(vector<int> &nums, int end){
        if(end==0)
            return nums[0];
        if(end==1)
            return max( nums[0], nums[1]);
        // two case , nums[end] is robbed or not
        return max( robCore(nums, end-2)+nums[end], robCore(nums, end-1)); //最后一个偷与不偷
        
    }
};
*/

class Solution {
public:
    int rob(vector<int>& nums) {
        int len = nums.size();
        if(len==0)
            return 0;
        int dp[len+1];  //dp[i]表示前面nums[0,.., i-1]里面的最大值
        dp[0]=0;
        dp[1]=nums[0];
        for(int i=1;i<len;i++)
            dp[i+1] = max(dp[i],nums[i]+dp[i-1]);
        for(int j=0;j<len+1; j++)
            cout<<dp[j]<<" ";
        cout<<endl;
        return dp[len];
    }
};
```
