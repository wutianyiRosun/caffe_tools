### 228. Summary Ranges
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```
//O(n)时间 O(1)空间
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if(nums.size()==0)
            return res;
        int start=nums[0];
        int cur=nums[0];
        for(int i=1; i<nums.size(); i++){
            if(nums[i]==cur+1){
                cur=nums[i];
                
            }
            else{  //nums[i]>cur+1
                if(cur==start){
                    res.push_back(to_string(start));
                }
                else{
                    res.push_back(to_string(start)+"->"+to_string(cur));
                }
                start=nums[i];
                cur=nums[i];
            }
        }
        if(cur==start){
            res.push_back(to_string(start));
        }
        else{
            res.push_back(to_string(start)+"->"+to_string(cur));
        }

        
        return res;
    }
};
```
