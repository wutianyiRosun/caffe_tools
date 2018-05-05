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
