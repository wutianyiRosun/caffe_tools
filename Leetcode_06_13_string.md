### 17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res_pre; //这个已处理好的子字符串的组合
        vector<string> res_cur; //保存当前组合， 组合当前遍历的字符digits[i]与res_pre
        if(digits.size()==0)
            return res_pre;
        for(int i=0;i<digits.size();i++){
            int num=digits[i]-'0';
            //tchar.clear();
            vector<char> tchar=int2chars(num);
            res_cur.clear();
            if(res_pre.size()!=0){
                for(int i=0;i<res_pre.size(); i++){
                    for(int j=0;j<tchar.size();j++)
                        res_cur.push_back(res_pre[i]+tchar[j]);
                }
            }else{
                for(int j=0; j<tchar.size(); j++){
                    string st="";
                    st+=tchar[j];
                    res_cur.push_back(st);
                }
                    
            }
            res_pre.clear();
            res_pre.assign(res_cur.begin(), res_cur.end());               
        }
        return res_cur;
    }
    vector<char> int2chars(int num){
        vector<char> tchar;
        if(num<7){
            for(int i=0;i<3;i++)
                tchar.push_back(char(97+(num-2)*3 +i));
        }else if(num==7){
            for(int assic=112; assic<=115; assic++)
                tchar.push_back(char(assic));
        }
        else if(num==8){
            for(int assic=116; assic<=118; assic++)
                tchar.push_back(char(assic));
        }else{
            for(int assic=119; assic<=122; assic++)
                tchar.push_back(char(assic));
        }
        return tchar;
    }
};
```
###  34. Search for a Range
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

```
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2, -1);
        if(nums.size()==0)
            return res;
        int start=0;
        int end = nums.size()-1;
        while(start<=end){
            int mid=(start + end)/2;
            if(nums[mid] < target){
                start=mid+1;
            }
            else if(nums[mid] > target){
                end = mid-1;
            }
            else{
                //find target
                int low=mid;
                while(low>=0 && nums[low]==nums[mid]){
                    low--;
                }
                low=low+1;
                int up = mid;
                while(up < nums.size() && nums[up]==nums[mid]){
                    up++;
                }
                up-=1;
                res[0]=low;
                res[1]= up;
                return res;
            }
        }
        return res;
    }
    
};
```



