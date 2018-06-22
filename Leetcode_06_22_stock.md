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
### 121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```
//Solution1: 枚举所有可能， 时间复杂度O(N^2)， 空间复杂度O(1)
/*
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit_max=0;
        for(int i=1;i<prices.size(); i++){
            for(int j=0;j<i;j++){
                if(prices[i]-prices[j]>profit_max)
                    profit_max=prices[i]-prices[j];
            }
        }
        return profit_max;
    }
};
*/
//Solution2: 时间复杂度O(N),空间复杂度O(1)
//我们定义一个变量minPrice，来记录当前最低股价， profit_max来记录最大收益
//我们遍历数组，if(prices[i]<minPrice) minPrice <- prices[i]
//否则计算收益 prices[i]-minPrice
class Solution{
public:
    int maxProfit(vector<int> & prices){
        if(prices.size()<=1)
            return 0;
        int minPrice=prices[0];
        int profit_max=0;
        for(int i=1; i<prices.size(); i++){
            if(prices[i]<minPrice){
                minPrice=prices[i];
            }
            else{
                //计算在这个时刻出售股票， 在minPrice买股票的收益
                if(prices[i]-minPrice > profit_max)
                    profit_max=prices[i]-minPrice;
            }
        }
        return profit_max;
    }
};

```
