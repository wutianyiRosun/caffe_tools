### 494. Target Sum
 You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int start=0;
        int end=nums.size()-1;
        int ways=0;
        findTargetSumWaysCore(nums, start, end, S, ways);
        return ways;
    }
    void findTargetSumWaysCore(vector<int>& nums, int start, int end, int target, int &ways){
        if (start==end){
            if(target==0 && nums[end]==0){
                ways+=2;
            }
            else if(target==nums[end] || target==(-1)*nums[end]){
                ways+=1;
            }
        }
        else{
            findTargetSumWaysCore(nums, start+1, end, target+nums[start], ways);
            findTargetSumWaysCore(nums, start+1, end, target-nums[start], ways);
        }
    }
};
```
### 560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:


Input:nums = [1,1,1], k = 2
Output: 2
```
//定义数组dp[], dp[i]表示子序列nums[0,..,i]之和
//对于以元素nums[j]结束的连续子序列，我们计算dp[j]-dp[i]==k, i=0,1,...,j-1,等号成立表示子序列nums[i+1,...,j]之和是k

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if(nums.size()==0)
            return 0;
        int len=nums.size();
        int dp[len]; //dp[i]表示子序列nums[0,..,i]之和
        dp[0]=nums[0];
        for(int i=1;i<len;i++){
            dp[i]=dp[i-1]+nums[i];
        }
        int count=0;
        for(int j=0;j<len;j++){
            for(int i=j-1; i>=0; i--){
                if(dp[j]-dp[i]==k)  //nums[i+1,...,j]
                    count+=1;
            }
            if(dp[j] == k)
                count+=1;
        }
        return count;
    }
};


//Solution2: 时间复杂度O(N^2), 空间复杂度O(1)
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count=0;
        for(int i=0; i<nums.size(); i++){
            int sum=0;
            for(int end=i; end<nums.size(); end++){
                sum+=nums[end];
                if(sum==k)
                    count+=1;
            }
        }
        return count;
    }
};
```
### 35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1
```
//二分查找,时间复杂度log(n)
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size=nums.size();
        if(target<=nums[0])  //比最小的还小
            return 0;
        if(target>nums[size-1])//比最大的还大
            return size;
        int start=0, end=size-1;
        while(start<=end){
            int mid= (start+end)/2;
            if(nums[mid]>=target && nums[mid-1]<target){  //则在区间【start, mid]  找出第一个大于等于target的数字nums[mid], return mid
                return mid;
            }
            else if (nums[mid]>target ){
                end=mid-1;
            }
            else{
                start = mid+1;
            }
        }
    }
};

```
### 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL)
            return l2;
        if(l2==NULL)
            return l1;
        ListNode* newhead=NULL;
        ListNode* pcur=NULL;
        ListNode* pcur1=l1;
        ListNode* pcur2=l2;
        while(pcur1!=NULL && pcur2!=NULL){
            //cout<<"pcur1->val= "<<pcur1->val<<" pcur2->val= "<<pcur2->val<<endl;
            if(newhead==NULL){
                if(pcur1->val >= pcur2->val){
                    newhead=pcur2;
                    pcur2=pcur2->next;
                    pcur=newhead;
                }
                else{
                    newhead=pcur1;
                    pcur1=pcur1->next;
                    pcur=newhead;
                }
            }
            else{
                if(pcur1->val >= pcur2->val){
                    pcur->next=pcur2;
                    pcur=pcur->next;
                    pcur2=pcur2->next;
                    
                }
                else{
                    pcur->next=pcur1;
                    pcur=pcur->next;
                    pcur1=pcur1->next;
                    
                }
            }
            //cout<<" pcur->val="<<pcur->val<<endl;
        }
        if(pcur1!=NULL){
            pcur->next=pcur1;
        }
        if(pcur2!=NULL){
            pcur->next=pcur2;
        }
        return newhead;
    }
};
```
### 56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.


```
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
//首先按start排序
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if(intervals.size()<=1)
            return intervals;
        sort(intervals.begin(), intervals.end(), [](auto& lhs, auto& rhs) {  return lhs.start < rhs.start; });
        vector<Interval> result;
        result.push_back(intervals[0]);
        for(int i=1; i< intervals.size(); i++){
            Interval &last=result.back();
            if(intervals[i].start<=last.end){
                last.end=max(last.end, intervals[i].end);
            }
            else{
                result.push_back(intervals[i]);
            }
        }
        return result;
    }
   
};
```
