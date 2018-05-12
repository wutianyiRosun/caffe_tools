### 67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

```
class Solution {
public:
    string addBinary(string a, string b) {
        int lena=a.size();
        int lenb=b.size();
        //反转字符串从低位开始做加法
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        string result;
        vector<int> sumseq(max(lena,lenb),0);
       
        if(lena< lenb)
            swap(a, b);
       
        sumseq= addBinaryCore(a, b); //默认a的长度大于等于b
        int i=sumseq.size()-1;
        //remove最高位连续的0
        while(i>0 && sumseq[i]==0){
            i--;
        }
        for(; i>=0; i--){
            result.push_back(sumseq[i]+'0');
        }
        //cout<<result<<endl;
        return result;
        
    }
    vector<int> addBinaryCore(string &a, string &b){
        int lenA=a.size();  //较长的字符串, size()函数统计不考虑字符串尾部的\0
        int lenB=b.size();  
        int  lenRes=lenA+1;
        vector<int> sumseq(lenRes,0);
        int i;
        for(i=0; i<lenB; i++){
            int temp= sumseq[i] + a[i]+b[i]-2*'0';
            sumseq[i]=temp%2;
            sumseq[i+1]=temp/2;  //进位标志
        }
        for(; i<lenA+1-1; i++){
            int temp = sumseq[i]+a[i]-'0';
            sumseq[i] = temp%2;
            sumseq[i+1] = temp/2;
        }
        return sumseq;
    }
};
```
### 541. Reverse String II
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original. 
```
class Solution {
public:
    string reverseStr(string s, int k) {
        if(s.size()<=1)
            return s;
        for(int i=0;i<s.size();i++)
            cout<<s[i];
        cout<<endl;
        for(int start=0; start<s.size(); start=start+2*k){
            int i=start, j=Min(start+k-1, s.size()-1);
            cout<<"i="<<i<<"  j="<<j<<endl;
            while(i<j){
                char temp=s[i];
                s[i++]=s[j];
                s[j--]=temp;
               
            }
        }
        return s;
    }
    int Min(int a,int b){
        return a>b?b:a;
    }
};
```
