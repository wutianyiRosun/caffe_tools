### 263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
```
class Solution {
public:
    bool isUgly(int num) {
        if(num<=0)
            return false;
        else if(num == 1)
            return true;
        else if(num%2==0){
             return isUgly(num/2);
        }
        else if(num %3==0){
            return isUgly(num/3);
        }
        else if(num % 5==0){
            return isUgly(num/5);
        }
        else
            return false;
    }
};
```
### 202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```
class Solution {
public:
    bool isHappy(int n) {
        if(n<=0)
            return false;
        set<int> mid;
        while(n!=1){
            int temp=n;
            if(mid.count(temp)==0)
                mid.insert(temp);
            else 
                return false; //重复出现了，进入循环
            int squaresSumOfDigits=0;
            while(temp!=0){
                int bit = temp%10;
                squaresSumOfDigits+= bit==0?0:bit*bit;
                temp= temp/10;
            }
            n= squaresSumOfDigits;
        }
        return true;
        
    }
};
```
