### 754. Reach a Number

 You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

```
//Solution: 首先对于target为负数的情况，最小步数应该等同于正数
//我们先一直朝右走，知道所走步数之和不小与target.当sum-target大于0时，则意味着我们在某个步骤需要往左走，假设为第i步，这时和相当于少
//了2×i(本来是sum=sum+i, 我们向左走sum=sum-i),因此当差异为偶数时，则返回步数，如果不为偶数则一直加直到为偶数
class Solution {
public:
    int reachNumber(int target) {
        target= abs(target);
        int sum=0;
        int count=0;
        while(sum<target){
            count++;
            sum+=count;
        }
        while( (sum-target)%2!=0){
            count++;
            sum+=count;
        }
        return count;
    }
};

```
