### 179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

```
//Solution: 我们首先定义两个数的大小  a, b我们先把二者转换为a_str, b_str, if a_str+b_str>b_str+ a_str成立， 则a>b
//我们把数组按上面的方式排序, 然后按顺序把这些数拼接（转出字符串直接加)
bool srt(int a,int b)  //降序排列
{
    string x=to_string(a);
    string y=to_string(b);
    return (x+y>y+x);
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        
        string res="";
        if(nums.size()==0)
            return res;
        //检查数组是否都是0
        int fg=1;
        for(int i=0;i<nums.size();i++)
            if(nums[i]!=0){ 
                fg=0; 
                break; 
            }
        if(fg==1)  //数组元素都是0， 则返回0
            return "0"; 
        sort(nums.begin(),nums.end(),srt);
        
        for(auto j:nums){
            cout<<j<<",";
            res+=to_string(j);
        }
        
        return res;
    }
};
```
