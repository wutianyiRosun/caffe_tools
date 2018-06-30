### 438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```

/*
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> char2num(26,0);
        vector<int> result_index;
        //cout<<"p.size()="<<p.size()<<endl;
        for(int i=0; i<p.size(); i++)
            char2num[p[i]-'a']= char2num[p[i]-'a']==-1? 1: char2num[p[i]-'a']+1;
         for(int i=0; i<char2num.size(); i++)
             cout<<char2num[i]<<",";
        cout<<endl;
        int len=p.size();
        int left=0, right=0;
        while(right<s.size()){
            if(char2num[ s[right++]-'a']-->0) len--;  //如果s[right]是出现在p中的字符，则len减1

            if(len==0)  //当前子序列合法
                result_index.push_back(left);
            //如果当前滑动窗口长度等于p.size(),则需要右移动left, 如果s[left]字符是p中的，则需要把len增加1
            if (right - left == p.size() && char2num[s[left++]-'a']++ >= 0) len++;
        }
        return result_index;
    }
};*/

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> char2num(26,-1);
        vector<int> result_index;
        for(int i=0; i<p.size(); i++)
            char2num[p[i]-'a']= char2num[p[i]-'a']==-1? 1: char2num[p[i]-'a']+1;
        int len=p.size();
        int left=0, right=0;
        while(right<s.size()){
            if(char2num[ s[right++]-'a']-->0){
                len--;
            }
            if(len==0)  //当前子序列合法
                result_index.push_back(left);
            if(right-left==p.size()){
                char2num[s[left]-'a']+=1;
                if(char2num[s[left]-'a']>=1){
                    len+=1;
                }
                left+=1;
            }
        }
        return result_index;
    }
};
```

### 242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

```
//Solution: 我们先用一个数组统计其中一个字符串中所有字母出现的次数，然后遍历另外一个字符串，如果字符对应的次数大于0，则次数数组减1，长度减1 ，最后只需判断
//长度是否为0即可， 时间复杂度O(N),空间复杂度O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size())
            return false;
        if(s.size()==0 && t.size()==0)
            return true;
        vector<int> char2num(26,0);
        for(int i=0; i<s.size(); i++)
            char2num[s[i]-'a']++;
        int len=s.size();
        for(int i=0; i<t.size(); i++){
            if(char2num[t[i]-'a']>0){
                char2num[t[i]-'a']--;
                len--;
            }
        }
        return len==0;
    }
};
```
