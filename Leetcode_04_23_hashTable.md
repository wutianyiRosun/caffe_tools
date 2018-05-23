### 347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    
    
    
    
```
//Solution1:先遍历nums,把对应元素存到一个set中，元素本身作为key,其出现次数作为value
//然后把set中<key,value>做为一个pair插入到优先队列，最后从优先队列pop前k个pair,去pair.second压人最后的vector<int> res
/*
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        for(int num : nums){
            map[num]++;
        }
        vector<int> res;
        // pair<first, second>: first is frequency,  second is number
        priority_queue< pair<int,int> > pq; 
        for(auto it = map.begin(); it != map.end(); it++){ //auto在声明变量的时候根据变量的初始值自动匹配其类型，简便
            printf("number= %d  f=%d\n",it->second, it->first);
            pq.push(make_pair(it->second, it->first));
        }
        for(int j=0;j<k;j++){
             res.push_back(pq.top().second);
             pq.pop();
        }
        return res;
    }
};
*/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> map;
        for(int num : nums){
            map[num]++;
        }
        vector<int> res;
        // pair<first, second>: first is frequency,  second is number
        priority_queue< pair<int,int> > pq; 
        for(auto it = map.begin(); it != map.end(); it++){ //auto在声明变量的时候根据变量的初始值自动匹配其类型，简便
            printf("number= %d  f=%d\n",it->second, it->first);
            pq.push(make_pair(it->second, it->first));
            //当优先队列长度大于len-k时，这个时候对头元素肯定是Top-K中的
            if(pq.size() > (int)map.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;
    }
};
```
### 202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
class Solution {
public:
    bool isHappy(int n) {
        if(n<=0)
            return false;
        set<int> mid;
        while(n!=1){
            int temp=n;
            if(mid.count(temp)==0)
                mid.insert(temp);
            else 
                return false; //重复出现了，进入循环
            int squaresSumOfDigits=0;
            while(temp!=0){
                int bit = temp%10;
                squaresSumOfDigits+= bit==0?0:bit*bit;
                temp= temp/10;
            }
            n= squaresSumOfDigits;
        }
        return true;
        
    }
};
```
