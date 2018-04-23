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
