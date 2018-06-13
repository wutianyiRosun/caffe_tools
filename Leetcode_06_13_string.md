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
