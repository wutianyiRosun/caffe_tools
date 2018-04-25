### 240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

//solution1: 考虑到该数组每行是从左到右顺序递增，每一列也是这样，这个性质对我们求解非常重要。我们想象一个非常大的矩阵我们寻找某个target是非常困难的事，能不能想办法把这个矩阵变小，在一个比较小的矩阵里查找是不是容易些。仔细观察我们发现只要把矩阵右上角的元素与当前target比较，如果右上角元素大于target，则当前列的所有元素都大于target，这时我们则可以把矩阵列数减1，同理当当前元素都小于target，则当前行的元素都小于target，则把矩阵行数加1得到新的子矩阵，如此循环下去，直到找到，或者遍历到左下角还没找到，则返回false
/*
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rowMax=matrix.size();
        if (rowMax==0)
            return false;
        int colMax=matrix[0].size();
        if(colMax==0)
            return false;
        
        return searchMatrixCore(matrix, 0, colMax-1, target);  //从右上角开始遍历
    }
    bool searchMatrixCore( vector<vector<int>>& matrix, int row, int column, int target){
        cout<<"row= "<<row<<"  column= "<<column<<endl;
        if(row==matrix.size()-1 && column==0){
            return matrix[row][0]==target;
        }
        if(matrix[row][column]==target)
            return true;
        else if(matrix[row][column]<target){//当前行元素都小于target
            if(row<matrix.size()-1) //还没到最后一行
                return searchMatrixCore(matrix, row+1, column, target);
            else
                return false;
        }  
        else{//matrix[row][column]>target 当前列的元素都大于target
            if(column>0)  //还没到第0列
               return searchMatrixCore(matrix, row, column-1, target);
            else
                return false;
        }      
            
    }
};*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rowMax=matrix.size();
        if (rowMax==0)
            return false;
        int colMax=matrix[0].size();
        if(colMax==0)
            return false;
        for(int i=0;i<rowMax; ){
            for(int j=colMax-1;j>=0;){   //从右上角开始遍历
                int cur=matrix[i][j];
                if( cur==target)
                    return true;
                else if(cur<target){ //当前一整行都小于target
                    if(i<rowMax-1)
                        i++;
                    else
                        return false;
                }
                else{   //当前一整列都大于target
                    if(j>0)  
                        j--;
                    else
                        return false;
                }
            }
        }
    }
   
};
