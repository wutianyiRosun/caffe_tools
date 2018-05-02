### 122. Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
             

```
/*
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<=1)
            return 0;
        int profit=0;
        vector<int> diff(prices.size()-1,0);
        for(int i=0;i<prices.size()-1; i++)
            diff[i]=prices[i]-prices[i+1];
        cout<<diff.size();
        for(int j=0;j<diff.size();j++){
            if(diff[j]<0)
                profit-=diff[j];
        }     
        return profit;
    }
};
*/
//Speed up
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<=1)
            return 0;
        int profit=0;
        for(int i=0;i<prices.size()-1; i++){
              int diff = prices[i]-prices[i+1];
              if( diff < 0){
                  profit-= diff;
              }
        }
        return profit;
    }
};
```
### 455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:

Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.


```
//soulution: 很容易知道满足贪心性质，把children greedy factors array g和 cookies array s分别从小到达排序，每次我们从g中取一个数g[i],然后从s中找一个大于等于g[i]且离g[i]距离最近的一个数，如果找到则结果加1,然后给第i+1个孩子分配蛋糕，
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int res=0;
        auto iter=s.begin();
        for(int i=0;i<g.size();i++){
            for(; iter!=s.end() ; ){
                if (*iter>=g[i]){
                    res+=1;
                    iter++;
                    break;
                }
                iter++;
            }
            if(iter==s.end())
                break;
        }
        return res;
    }
};
```


