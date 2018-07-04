### 406. Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

```
//Solution: 我们给队列先排个序，按照身高高的排前面，如果身高相同，则第二个数小的排前面。
//然后我们新建一个空的数组，遍历之前排好序的数组，然后根据每个元素的第二个数字，将其插入到res数组中对应的位置，参见代码如下
class Solution {
public:
    static bool cmp(pair<int,int> a, pair<int, int> b){
        if(a.first==b.first)
            return a.second<b.second;
        return a.first > b.first;
    }
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(), people.end(), cmp);
        vector<pair<int, int>> res;
        for( auto it: people)
            res.insert(res.begin()+it.second, it);
        return res;
    }
};
```
### 394. Decode String
 Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```
//Solution: 最直观的解法就是我们从头开始遍历字符串，遇到非']'字符，则压入到一个栈，遇到']'则不压入栈，从当前stack中把与当前']'匹配的括号中间的字符给读出来， 
//然后再读出数字，进行复制n次，然后再压人栈中,知道遍历最后一个字符，这样stack中保存的就是我们要的字符串，把它读取出来，再逆序
class Solution {
public:
    string decodeString(string s) {
        stack<char> ass_stack;
        string res="";
        string tempstr="";
        for(int i=0; i<s.size(); i++){
            cout<<"i= "<<i<<endl;
            if(s[i]!=']'){
                ass_stack.push(s[i]);
            }
            else{ // s[i]==]
                while(ass_stack.top()!='['){
                    tempstr+=ass_stack.top();
                    ass_stack.pop();
                }
                ass_stack.pop(); //pop '['
                //处理当前k[  ]区域的字符
                int nums= 0;
                int bits=1;
                while(ass_stack.size()>0 && ass_stack.top()>='0' && ass_stack.top()<='9'){ //读取数字K,小心多位数清空
                    cout<<"bits= "<<bits<<endl;
                    nums=nums+bits*(ass_stack.top()-'0'); 
                    ass_stack.pop(); // pop 'k'
                    bits=bits*10;
                }
                cout<<"nums= "<<nums<<endl;               
                string repeatStr=tempstr;
                while(nums>1){
                    repeatStr+=tempstr; //重复字符串直接加
                    nums--;
                }
                for(int j=repeatStr.size()-1; j>=0; j--){
                    ass_stack.push(repeatStr[j]);
                }
                repeatStr="";
            }
            tempstr="";
       }
       while(ass_stack.size()>0){
           res+=ass_stack.top();
           ass_stack.pop();
       }
        reverse(res.begin(), res.end()); //逆转字符串
        return res;
    }
};
```
### 22. Generate Parentheses
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

```
//Solution: 我们把这个问题看出一系列决策问题， 给定一个数n,我们需要2n次操作，每次分配( 或者)，但需要保证有效性，匹配，即剩余的右括号数量大于等于剩余的左括号数量
//根据这个规则，写出递归函数
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        if(n<=0)
            return res;
        string temp="";
        GenParCore(n, n, temp, res);
        return res;  
    }
    void GenParCore(int left_n,int right_n, string temp, vector<string> & res){
        //cout<<"left= "<<left_n<<" right_n= "<<right_n<<" "<<temp<<endl;
        if(left_n==0 && right_n==0)
            res.push_back(temp);
        if(right_n>=left_n){
            if(left_n>=1)
                GenParCore(left_n-1, right_n,temp+"(", res);
            if(right_n>=1)
                GenParCore(left_n, right_n-1, temp+")", res);
        }
        
    }
};
```
