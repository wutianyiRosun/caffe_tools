### 223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

###
```
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        
        int area1 = abs(A-C) * abs(B-D);
        int area2 = abs(E-G) * abs(F-H);
        int x1=0,x2=0; //重合小矩形的左下角、右上角横坐标
        if(C<=G && E<=C){
            x2 = C;
            x1 = max(A,E);
        }else if(C>G&& A<G){
            x1 = max(A,E);
            x2 = G;
        }
        else{
            x1=x2=0;
        }
        int y1=0, y2=0; //重合小矩形的左下角、右上角的纵坐标
        if(H<=D && H>B){
            y2= H;
            y1 = max(B, F);
        }else if(H>D && F<D){
            y2=D;
            y1=max(B, F);
        }else{
            y1=y2=0;
        }
        int commonArea =abs(y2-y1)* abs(x2-x1);
        return area1+area2-commonArea;
        
    }
};
```
