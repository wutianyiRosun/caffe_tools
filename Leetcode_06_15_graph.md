### 206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //do with case empty list or single-node list
        if(head==NULL || head->next== NULL)
            return head;
        ListNode *Ppre=NULL;
        ListNode *Pcur=head;
        ListNode * Pnext=Pcur->next;
        ListNode * newhead=NULL;
        while(Pcur!=NULL){
            Pcur->next=Ppre;
            Ppre=Pcur;
            Pcur=Pnext;
            if(Pnext!=NULL) //当pcur指向最后一个节点时， Pnext此时已经指向了NULL节点
                Pnext=Pnext->next;
        }
        newhead= Ppre;
        return newhead;
    }
};
```
### 207. Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
             
```
//这个问题等价与判断邻接矩阵是否有cycle,然后有cycle则不能完成
//判断图结构的，可以通过计算每个节点的出度(outDegree)或者入度(inDegree)
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        //construcing neghubors list
        vector<vector<int>> graph(numCourses, vector<int>(0));  //邻接链表， graph[i]是所有指向节点i的list
        vector<int> outDegree(numCourses,0);   
        for(int i=0; i<prerequisites.size(); i++){
            auto u= prerequisites[i];
            graph[u.second].push_back(u.first);   //second <---- first  //[first, second]  second-->first  
            outDegree[u.first]+=1;
        }
        
        //collect the set of node's indegree is zero
        queue<int> objSet;
        for(int i=0; i<numCourses; i++){
            if(outDegree[i]==0)
                objSet.push(i);
        }
        
        //check cycle
        while(objSet.size()>0){
            int u=objSet.front();
            objSet.pop();
            //delete all edge which is start from u
            for(auto v: graph[u]){//edge: v--->u
                outDegree[v]--; //delete v--->u
                if(outDegree[v]==0){
                    objSet.push(v);
                }
            }
        }
        
        for(int i=0; i<numCourses; i++){
            if(outDegree[i]!=0)
                return false; //存在出度outDegree不为0的节点，则说明有cycle
        }
        return true;
        
    }
};
/*
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<vector<int>> graph(numCourses,vector<int>(0));  //graph[i]表示从i节点出发的所有边的另一节点的集合
        vector<int> indegree(numCourses,0);
        for(auto u:prerequisites){
            graph[u.second].push_back(u.first);  
            cout<<u.first<<endl;  //[first, second]  second-->first
            indegree[u.first]++;
            }
        queue<int> q;
        for(int i=0;i<indegree.size();i++){
            if(indegree[i]==0)
                q.push(i);
        }
        while(!q.empty()){
            int u=q.front();
            q.pop();
            for(auto v:graph[u]){
                indegree[v]--;
                if(indegree[v]==0)
                    q.push(v);
            }
            
        }
        for(int i=0;i<indegree.size();i++){
            if(indegree[i]!=0)
                return false;
        }
        return true;

    }
};*/
```
### 210. Course Schedule II
here are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]

Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
             
             
```
//1.constructing directed graph, and check whether existing cycle. true: return empty array, false: return one possible
class Solution {
public:

       vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        //constructing Adjacency List, and using indegree for checking cycle
class Solution {
public:
    vector< vector<int> > adjList(numCourses, vector<int>(0) );  //adjList[i]表示从节点i指向的所有节点的list
        vector<int> inDegree(numCourses, 0);
        for(auto item: prerequisites){  //item: [first, second], second--->first
            adjList[item.second].push_back(item.first);
·            inDegree[item.first]+=1;
        }
        
        //Collect node whose inDegree is zero
        queue<int> zeroD;
        for(int i=0; i< numCourses; i++){
            if(inDegree[i]==0)
                zeroD.push(i);
        }
        //construcing the order o taking courses
        vector<int> orderCourse;
        while(zeroD.size()>0){
            int u= zeroD.front();
            zeroD.pop();
            orderCourse.push_back(u);
            for(auto v: adjList[u]){
                //u--->v
                inDegree[v]--;
                if(inDegree[v]==0){
                    zeroD.push(v);
                }
            }
        }
        //check all node's indegree are 0,
        for(int i=0; i<numCourses; i++){
            if(inDegree[i]!=0){
                orderCourse.clear();
                return orderCourse;
            }
        }
        
        return orderCourse;
    }
};
```
### 221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.size()==0)
            return 0;
        if(matrix[0].size()==0)
            return 0;
        int m=matrix.size();
        int n=matrix[0].size();
        vector< vector<int>> dp(m, vector<int>(n,0));
        //初始化第一行
        int res=0;
        for(int i=0; i<n; i++){
            if(matrix[0][i]=='1'){
                dp[0][i]=1;
                res=max(res, dp[0][i]);
            }
        }
        //初始化第一列
         for(int i=0; i<m; i++){
            if(matrix[i][0]=='1'){
                dp[i][0]=1;
                res=max(res, dp[i][0]);
            }
        }
        
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                if(matrix[i][j]=='1'){
                    dp[i][j]= min( min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1;
                    res=max(res, dp[i][j]*dp[i][j]);
                }
                else
                    dp[i][j]=0;
                
            }
        }
        return res;
    }
};
```
