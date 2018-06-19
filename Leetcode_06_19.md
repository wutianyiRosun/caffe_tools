### 20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
```
//solution, 遍历字符串，遇到‘（’，‘{’, '['，则压入栈，遇到另外三种则看栈顶元素是否能与之进行配对
class Solution {
public:
    bool isValid(string s) {
        if(s.size()==0)
            return true;
        stack<char> ass_stack;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
                ass_stack.push(s[i]);
            }
            else if(s[i]==')'){
                if(ass_stack.size()==0 || ass_stack.top()!='(')
                    return false;
                else
                    ass_stack.pop();
            }
            else if(s[i]==']'){
                if(ass_stack.size()==0 || ass_stack.top()!='[')
                    return false;
                else
                    ass_stack.pop();
            }
            else if(s[i]=='}'){
                if(ass_stack.size()==0 || ass_stack.top()!='{')
                    return false;
                else
                    ass_stack.pop();
            }
        }
        return ass_stack.empty();
    }
};
```
### 75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example 1:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?

```
//Solution: 首先定义长度为3的数组， len[3], len[j],j=0,1,2。 我们从头开始遍历数组nums,假设当前元素nums[i]. len[j]表示子序列nums[0,...,i-1]中元素j出现的次数
//并且子序列nums[0,...,i-1]是排好序的
// case 0: if(nums[i]==2), 无需操作
// case 1: if(nums[i]==1 && len[2]>0), 我们交换该元素与子序列中第一个为2的元素, swap(nums[i], nums[len[0]+len[1]])
// case 2: if(nums[i]==0 && len[1]+len[2]>0), 此时我们最多要做两次交换， 如果子序列nums[0, ..., i-1] 有元素1，则把该元素先与第一个为1的元素交换，如果有元素2则把该元素与第一个
//为2的元素进行交换， 
class Solution {
public:
    void sortColors(vector<int>& nums) {
        if(nums.size()<=1)
            return;
        vector<int> len(3, 0); //初始化记录元素个数的数组
        for(int i=0; i<nums.size(); i++){
            if(nums[i]==1 && len[2]>0){  //交换该元素与子序列中第一个为2的元素
                int temp= nums[i];
                nums[i]= nums[len[0]+len[1]];
                nums[len[0]+len[1]]=temp;
                len[1]+=1;  //元素1的数量增加1个
                
            }
            else if(nums[i]==0 && len[1]+len[2]>0){
                if(len[1]>0){ //子序列中存在元素1，则需要交换该元素与第一个为1的元素
                    int temp=nums[i];
                    nums[i]=nums[len[0]];  //nums[i]=1
                    nums[len[0]]=temp; 
                    //len[0]+=1;
                    if(len[2]>0){  //如果子序列中还存在元素2， 则需要把位置i的元素与第一个为2的元素进行交换
                        int temp=nums[i];
                        nums[i]=nums[len[0]+len[1]];
                        nums[len[0]+len[1]]=temp;
                    }
                    else{
                        nums[len[0]+len[1]]=1;
                    }
                }else if(len[1]==0 && len[2]>0){ //子序列中只存在元素2，不存在元素1
                    int temp=nums[i];  //交换当前元素与第一个为2的元素
                    nums[i]=nums[len[0]];
                    nums[len[0]]=temp;
                }
                len[0]+=1;       
            }
            else{
                len[nums[i]]+=1;
            } 
        }
    }
};
```

