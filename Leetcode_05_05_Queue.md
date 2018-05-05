### 225. Implement Stack using Queues

Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Notes:

    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
```
//对于这个题，用队列来实现一个拥有push、pop、top、empty()功能的stack
//我们发现，对于push,操作与queue一样，直接push, 而pop()操作用一个队列是无法实现， 队列自己提供的front()是返回最先进队的元素，因此我们在这里考虑用两个队列来实现，我们保证任何时候，这两个队列至多只有一个队列非空，另外一个队列是在进行stack.pop()时后用，即把非空队列的所有元素(最后一个元素除外)顺序进入空的队列， 然后把那个最后元素作为返回值，并进行delete. 而对于stack.push(),如果有队列不为空，则把元素Push到这个队列，如果两个都为空，任意选折一个，只要每次保持选同一个；对于stack.empyt()则更简单。 而stack.top()是取得最后一个入stack的元素，则用非空队列的back()



class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
      
    }
    queue<int> q1;
    queue<int> q2;
    /** Push element x onto stack. */
    void push(int x) {
        if(q1.size()>0){
            q1.push(x);
        }
        else if(q2.size()>0){
            q2.push(x);
        }
        else //q1 and q2 are empty
            q1.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    //去除最后一个插入的元素
    int pop() {
        if(q1.size()>0 && q2.size()==0){
            //把q1的元素（最后一个元素除外） 放到q2中,并把q1最后一个元素作为返回值,同时delete
            while(q1.size()>1){
                q2.push(q1.front());
                q1.pop();
            }
            int res=q1.back(); // as return value
            q1.pop();  //remove the element from q1
            return res;
            
        }else if(q2.size()>0 && q1.size()==0){
            //把q2的元素（最后一个元素除外） 放到q1中, 并把q2最后一个元素作为返回值，同时delete
            while(q2.size()>1){
                q1.push(q2.front());  //q2的元素顺序出队，进入q1
                q2.pop();
            }
            int res = q2.back();
            q2.pop(); //remove the element from q2
            return res;
        }else{  //q1 and q2 are empty
            return NULL;
        }
    }
    
    /** Get the top element. */
    //得到最后一个元素，但还是保存在队列中,queue.back()函数返回队里最后插入元素
    int top() {
        if(q1.size()>0)
            return q1.back();
        else if(q2.size()>0)
            return q2.back();
        else //q1 and q2 are empty
            return NULL;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        if(q1.size()==0 && q2.size()==0)
            return true; //stake is empty, return true;
        else
            return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */
 ```
 
 ### 232. Implement Queue using Stacks
 
  Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

```
//利用stack实现queue, 对于queue.push()操作比较好说，直接用stack.push()
//对于queue.pop()操作是得到最先插入的元素，同时还要delete it, 我们看标准的stack()，如果只有一个stack,我们只能取最后插入的元素，因此我们想要借用一个辅助的stack来帮助我们实现queue.pop()， 通过把非空stack的元素（第一个元素除外)，压人那个空的stack,这样我们就能得到最先插入的元素，同时可以删除它， 然后再把刚刚出stack的所有元素顺序入stack 。对于queue.peek()操作，与queue.push()实现机制类似，差异在于处理最后一个元素，我们获取该元素之后，不删除它，而是把它也插入那个空的stack,最后我们再把所有元素都从另外的那个stack进行出stack,然后入这个stack

class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    stack<int> st1;
    stack<int> st2;
    /** Push element x to the back of queue. */
    void push(int x) {
        if(st1.size()>0)
            st1.push(x);
        else
            st2.push(x);
        
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(st1.size()>0){ //st1非空，则把st1的所有元素（最后插入的元素除外）出stack，同时入st2
            while(st1.size()>1){
                st2.push(st1.top());
                st1.pop(); //delete from stack st1
            }
            int res= st1.top();  //the last element of st1
            st1.pop(); //delete the last element from st1
            //st1 is empty, 
            while(st2.size()>0){
                st1.push(st2.top());
                st2.pop();
            }
            return res;
            
        }else if(st2.size()>0){ //st2非空，则把st2的所有元素（最后插入的元素除外）出stack，同时入st1
            while(st2.size()>1){
                st1.push(st2.top());
                st2.pop(); //delete from stack st2
            }
            int res= st2.top();  //the last element of st2
            st2.pop(); //delete the last element from st2
             //st2 is empty, 
            while(st1.size()>0){
                st2.push(st1.top());
                st1.pop();
            }
            return res;
            
        }
        else
            return NULL;
        
    }
    
    /** Get the front element. */
    int peek() {
        if(st1.size()>0){ //st1非空，则把st1的所有元素出stack，同时入st2，但取出最开始插入的元素
            while(st1.size()>1){
                st2.push(st1.top());
                st1.pop(); //delete from stack st1
            }
            int res= st1.top();  //the last element of st1
            st2.push(st1.top()); //saving the last element of st1
            st1.pop(); 
            //st1 is empty, 
            while(st2.size()>0){
                st1.push(st2.top());
                st2.pop();
            }
            return res;
            
        }else if(st2.size()>0){ //st2非空，则把st2的所有元素出stack，同时入st1, 但取出最开始插入的元素
            while(st2.size()>1){
                st1.push(st2.top());
                st2.pop(); //delete from stack st2
            }
            int res= st2.top();  //the last element of st2
            st1.push(st2.top());  //saving the last element of st2
            st2.pop(); 
             //st2 is empty, 
            while(st1.size()>0){
                st2.push(st1.top());
                st1.pop();
            }
            return res;
            
        }
        else
            return NULL;
        
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        if(st1.size()==0 && st2.size()==0)
            return true;
        else
            return false;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */
 ```
