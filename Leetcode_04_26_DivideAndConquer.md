### 493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

Example2:

Input: [2,4,3,5,1]
Output: 3

```
//根据题中所提出的逆序对，我们很容易联想到归并排序的思想来解决这个题。
//每次Merge的时候统计符合要求的逆序对，然后进行排序。
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        if(nums.size()<=1)
            return 0;
        int count=0; 
        vector<int> res=reversePairsDivide(nums, 0, nums.size()-1, count);
        for(int i=0;i<res.size();i++)
            printf("%d\t",res[i]);
        return count;
    }
    vector<int> reversePairsDivide(vector<int>& nums, int left, int end, int &count){
        //cout<<"left="<<left<<" end="<<end<<endl;
        vector<int> subarray_count;
        if(end-left>0){
            int mid=(left+end)/2;
            vector<int>  LsubArray = reversePairsDivide(nums, left, mid, count );
            vector<int>  RsubArray = reversePairsDivide(nums, mid+1, end, count);
            subarray_count = reversePairsMerge(LsubArray, RsubArray, count);
           
        }
        else{
            subarray_count.push_back(nums[left]);

        }
        return subarray_count;
    }
    vector<int>  reversePairsMerge(vector<int> &LsubArray, vector<int> &RsubArray, int &count){
        int len=LsubArray.size()+RsubArray.size();
        cout<<"two subArray len="<<len<<endl;
        vector<int> tmp(len);
        cout<<"LsubArray:  ";
        for(int i=0;i<LsubArray.size();i++)
            cout<<LsubArray[i]<<",";
        cout<<endl;
        
        cout<<"RsubArray:";
        for(int i=0;i<RsubArray.size();i++)
            cout<<RsubArray[i]<<",";
        cout<<endl;
        
        //统计合并的子数组逆序对个数
        int Lleft=0, Rleft=0;
        for(int i=0;i<LsubArray.size();i++){
            int j=0;
            while(j!=RsubArray.size() &&LsubArray[i]>2*RsubArray[j] )
                j++;
            count+=j;
        }
        for(int k=0;k<len;k++){
            if( LsubArray[Lleft]>RsubArray[Rleft] && Rleft<(RsubArray.size()) ){
            
                tmp[k] = RsubArray[Rleft];
                Rleft++;
                
            }else if(LsubArray[Lleft]<RsubArray[Rleft] && Lleft<(LsubArray.size())){
                tmp[k] = LsubArray[Lleft];
                Lleft++;
            }
            else if(Lleft==LsubArray.size()){
                tmp[k]=RsubArray[Rleft];
                Rleft++;
            }
            else{ //if(Rleft==RsubArray.size()){
                tmp[k]=LsubArray[Lleft];
                Lleft++;
            }
        }
        cout<<"current count="<<count;
        cout<<endl;
        cout<<"two subArray sort tmp:";
        for(int i=0;i<tmp.size();i++)
            cout<<tmp[i]<<",";
        cout<<endl;
        return tmp;
    }
};
/*

class Solution {
public:
    int sort_and_count(vector<int>::iterator begin, vector<int>::iterator end) {
        if (end - begin <= 1)
            return 0;
        auto mid = begin + (end - begin) / 2;
        int count = sort_and_count(begin, mid) + sort_and_count(mid, end);
        for (auto i = begin, j = mid; i != mid; ++i) {
            while (j != end and *i > 2L * *j) //左子数组i指向的元素大于 右子数组索引从0到j指向元素的2倍 个数j-mid
                ++j;
            count += j - mid;
        }
        inplace_merge(begin, mid, end);
        return count;
    }

    int reversePairs(vector<int>& nums) {
        return sort_and_count(nums.begin(), nums.end());
    }
};*/
```
