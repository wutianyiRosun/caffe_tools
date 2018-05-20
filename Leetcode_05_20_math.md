### 365. Water and Jug Problem

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
```
//可以测量z的条件是， x和y的最大公约数不为0，且该最大公约数是z的一个因数
class Solution {
public:
   
    int gcd(int x, int y)//辗转相除法求最大公约数
    { 
       int max_v=max(x,y);
       int min_v=min(x,y);
       if(min_v==0)
           return 0;
       if(max_v%min_v==0)
           return min_v;
       else
           return gcd(min_v, max_v%min_v);
    }
    bool canMeasureWater(int x, int y, int z) {
        if(!gcd(x,y))return z == 0;
        return (x + y >= z) && (z % gcd(x,y)) == 0;
    }
};
```

### 397. Integer Replacement
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

```
//我们做一下贪心算法，当n为偶数时，我们以n/2替代
//当n为奇数时，分两种情况
//case1: 当(n+1)/2为偶数时，则以n+1替代n
//case2: 当(n-1)/2为偶数时，则以n-1替代n
//我们可以证明对于任意一个奇数n,  (n+1)/2 + (n-1)/2中必然有一个为奇数，一个为偶数；
//证明，我们用反证法，对于上面假设不成立，即二者之和(n+1)/2 + (n-1)/2 == 2k为偶数(两个偶数相加， 两个基数相加)--->n=2k,推出n为偶数矛盾
//特殊输入 1，2，3, INT_MAX
class Solution {
public:
    int integerReplacement(int n) {
        if(n==1) return 0;
        if(n==2) return 1;
        if(n==3) return 2;
        if (n == INT_MAX) return 32; 
        if(n%2==0){
           return 1+integerReplacement(n/2);  
        }
        else if( (n+1)%4==0){//n为奇数，且(n+1)/2为偶数
            return 1+integerReplacement(n+1); 
        }
        else //n为奇数，且(n-1)/2为偶数
            return 1+integerReplacement(n-1); 
    }
   
};
```
### 453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
```
//假设最小移动数为m_step;最小元素每一次都会增加1， 我们用n表示list长度，sum表示其和， min表示其最小元素，则m_step次增加之后
// sum+m_step*(n-1)=(min + m_step)*n ==> m_step= sum-min*n
class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n=nums.size();
        int sum=nums[0];
        int min=nums[0];
        for(int i=1;i<=n-1;i++){
            sum+=nums[i];
            if(min>nums[i])
                min=nums[i];
        }     
        cout<<"len= "<<n<<" sum="<<sum<<" min="<<min<<endl;
        int m_step=sum-min*n;
        return m_step;
        
        
    }
};
```
### 396. Rotate Function solution2 is still preblem
Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].

Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:

A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
```
//Solution1: O(N^2)复杂度
/*class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int max=0;
        int n=A.size(); 
        for(int i=0;i<n;i++) //F(0)
            max+=i*A[i];
        //computing F[i]
        for(int i=1;i<n;i++){
            int start=0, temp=0;
            for(int j=n-i; j<n;j++){
                temp+=start*A[j];
                start++;
            }
            for(int k=0;k<n-i;k++){
                temp+=start*A[k];
                start++;
            }
            if (temp>max)
                max=temp;     
        }
        return max;
    }
};
*/

//Solution2: O(N)复杂度
//仔细观察我们可以发现： F(k)=(k,  k+1,k+2, ... , n-2, n-1,0,1, ... ,k-1)*A
//                   F(k+1)=(k+1,k+2,k+3, ... , n-1, 0,  1,2, ... ,k  )*A
//              F(k+1)-F(k)=(1,  1,  1,   ... , 1,   1-n,1,1, ... , 1)*A=sum(A)-n*A[n-1-k]----> F(k+1)= F(k)+sum(A)-n*A[n-k-1]
class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int sum=0;
        int max=0;
        int n=A.size(); 
        for(int i=0;i<n;i++){
            max+=i*A[i];//F(0)
            sum+=A[i];
        } 
        cout<<"max="<<max<<" sum="<<sum<<endl;
        //computing F[k]
        int Fpre= max;
        for(int k=1;k<n;k++){
           int Fcur=Fpre+sum-n*A[n-k-1];
           if(Fcur>max)
               max=Fcur;
           Fpre= Fcur;
        }
        return max;
    }
};
```
