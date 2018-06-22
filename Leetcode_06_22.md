### 309. Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

```
//Solution1:假设n=prices.size() 我们定义数组buy[n], buy[i]表示在第i天是否进行买，对应的收益
//数组sell[n], sell[i]比表示在第i天是否进行卖，对应的收益， 原问题等价于求sell[n-1], 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int last_sell = 0, last_buy = INT_MIN, last_cooldown = 0;
        int sell = 0, buy = 0, cooldown = 0;
        for(auto price:prices) {
            buy = max(last_buy, last_cooldown - price); //前者表示当前不买，即收益为last_buy时的收益， 后者表示当前买,即为以上次冷却的收益减去当前的股票价
            sell = max(last_sell, last_buy + price);//前者表示当前不卖的收益，收益则是last_sell，后者表示当前卖,即为上次买了之后的收益加当前股票价
            cooldown = max(last_cooldown, last_sell); //前者表示当前继续保持冷却， 后者表示从上次买股票之后进入冷却
            last_buy = buy;
            last_sell = sell;
            last_cooldown = cooldown;
        }
        return sell;
    }
};
```
