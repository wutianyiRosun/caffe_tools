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
