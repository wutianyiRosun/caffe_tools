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

