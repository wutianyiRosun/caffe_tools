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
