### 239. Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window.  time the sliding window moves right by one position. Return the max 
sliding window.
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
 ```
 class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> max_res;
        deque<int> slidingWin;  //该队列存对应元素的索引
        if(nums.size()==0)
            return max_res;
        for(int i=0;i<k;i++){
            while(slidingWin.size()>0 && nums[i] > nums[slidingWin.back()])
                slidingWin.pop_back();
            slidingWin.push_back(i); //存储元素值大的索引
        }
        for(int i=k; i<nums.size(); i++){
            max_res.push_back( nums[slidingWin.front()]);
            //cout<<"i="<<i<<" current val="<<nums[i]<<"   slidingWin.size()= "<<slidingWin.size()<<endl;
            //printDeque(slidingWin);
            //slidingWin保存区间 [i-k+1, i] ,k个元素的最大值
            while(slidingWin.size()>0 && nums[i]>=nums[slidingWin.back()])  //当前元素大于队列sildingWin后面一部分元素
                slidingWin.pop_back();
            if(slidingWin.size()>0 && slidingWin.front() <= i-k) //队列的首元素已经滑出滑动窗口了
                slidingWin.pop_front();
            //cout<<"after op, slidingWin.size()= "<<slidingWin.size()<<endl;
            //printDeque(slidingWin);
            slidingWin.push_back(i);
             //printDeque(slidingWin);
        }
        max_res.push_back( nums[slidingWin.front()]);
        return max_res;
    }
    void printDeque(deque<int> nums){
        for(auto item: nums)
            cout<<item<<",";
        cout<<endl;
    }
};
```
