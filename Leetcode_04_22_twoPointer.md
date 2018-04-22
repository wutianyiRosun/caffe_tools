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

### 209. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

//solution1:关于这个最小连续子序列和问题，我们用mem_len[i]表示序列以第i(i=0,1,2....)个元素结束的子序列和大于等于s的最小长度
//最后原问题的解一定是mem_len[i]，(i=0,1,...,n-1, n为序列长度)中最小的值
//Time complexity: O(N^2), Space complexity: O(N)
```
/*
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.size()==0||s<=0)
            return 0;
        int len=nums.size();
        int mem_len[len];
        for(int i=0;i<len;i++){
            mem_len[i]=-1; //不存在子序列和大于s
            int j=i;
            int sum=0;
            do{
                sum+=nums[j];
                if(sum>=s){
                    mem_len[i]=i-j+1;
                    break; //跳出do while循环
                }
                j--;
                
            }while(j>=0);
        }
        bool exist=0;//0: 不存在; 1:存在这样子序列
        int minlen=0;
         printf("mem_len:");
        for(int i=0;i<len;i++){
            printf(" %d\t",mem_len[i]);
            if(mem_len[i]!=-1 && exist==0){
                exist=1;
                minlen=mem_len[i];
            }
            if(mem_len[i]!=-1 && exist==1){
                minlen=min(minlen, mem_len[i]);
            }
        }
        return exist==0?exist:minlen;
        
    }
};
*/
//Soution2: 思路同solution1,Time complexity: O(N^2), Space complexity: O(1)
/*
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.size()==0||s<=0)
            return 0;
        int len=nums.size();
        bool exist=0;//0: 不存在; 1:存在这样子序列
        int minlen=0;
        for(int i=0;i<len;i++){
            int j=i;
            int sum=0;
            do{
                sum+=nums[j];
                if(sum>=s ){
                    if(exist==0){
                        minlen=i-j+1;
                        exist=1;
                        break;
                    }else{
                        minlen=min(minlen, i-j+1);
                        break; //跳出do while循环
                    }
                }
                j--;    
            }while(j>=0);
        }
        return exist==0?exist:minlen;
        
    }
};*/

//Solution3: 考虑到Solution2中有很多计算重复，我们换个思路把;
//对于序列，我们遍历，当前元素索引为i,我们累计前i个元素和，直到第一次找到sum>=s,我们在右移pleft,减少子序列长度到最短
//当我们遍历到i+1元素时,最短子序列的起始元素就是上一次的pleft,更左边的元素就不用考虑了，因为那样长度更长了，无需考虑

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.size()==0||s<=0)
            return 0;
        int len=nums.size();
        int minlen=INT_MAX;
        int sum=0;
        int pleft=0;
        for(int i=0;i<len;i++){
            sum=sum+nums[i];
            while(sum>=s){
                minlen=min(minlen, i-pleft+1);
                sum-=nums[pleft];
                pleft++;  
            }
        }
        return minlen==INT_MAX?0:minlen;
        
    }
};
```
