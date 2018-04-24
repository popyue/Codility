# Rakuten Codility


* [Rectengle Area](#rectengle)

<h2 id=rectengle>Rectengle Area</h2> 

### 題目:

A rectengle is called rectlinear if its edge are all parallel to coordinate axes.Such a rectengle can be described by specifying the coordinates of its lower-left and upper-right corners.

Write a function:

```
    def  solution(K,L,M,N,P,Q,R,S)
```
that, given eight integers representing two rectlinear rentengles(one with lower-left corner(K,L) and upper-right corner(M,N), and another with lower-left corner(P,Q) and upper-right corner(R,S)),return the area of the sum of the rectengles. If the rectengles intersect, the area of their intersection should be count only once. The function should return -1 if the area of the sum exceeds 2,147,483,647.

For example, given integers:

```
K = -4, L = 1,  M = 2, N = 6
P = 0,  Q = -1, R = 4, S = 3
```
the function should return 42.
![](https://i.imgur.com/ADxuJMF.png)

The area of the first rectengle is 30, the area of the second rectengle is 16 and the area of their sum is 42 (since their intersection area is 4).

Assume that:

* K,L,M,N,P,Q,R and S are integers within the range [-2,147,483,647 ... 2,147,483,647];
* K < M ;
* L < N ;
* P < R ;
* Q < S ;

Comlexity:

* expected worst-case time complexity is O(1)
* expected worst-case space complexity is O(1)


### 題目解釋：

根據題目的說明，會給予6個值(K,L,M,N,P,Q,R,S)，6個執行成 4個座標，分別為兩個長方形的左下(K,L)、(P,Q)與右上(M,N)、(R,S)的兩個座標，透過長方形的兩個座標求出長與寬，並進一步計算兩個長方形之面積。
程式最後要回傳兩個長方形的面積總和，
但有兩項例外條件必須注意:
1. 若兩個長方形有相交(重疊)的面，則該面的面積只能被計算一次。
2. 若最後的值大於2,147,483,647 則回傳-1 。

### 程式碼解題方向：

1. 先計算兩個矩形各自的面積
2. 計算相交的面積之前，要先知道相交的區塊的長及寬
3. 計算相交的方式，一開始會認為事先判斷一個矩形的頂點是否存在另一個矩形的內部，
   但會有一種相交狀況是矩形的頂點都沒有在另一個矩形的內部(圖(3))，這樣會有Bug
![](https://i.imgur.com/rLTP6eg.png)
4. 所以改變一下想法，判断两个矩形的中心坐標的水平和垂直距離，只要這兩個值滿足以下條件就會相交。

假設：
    
    矩形A的寬 Wa = Xa2-Xa1 高 Ha = Ya2-Ya1
    矩形B的寬 Wb = Xb2-Xb1 高 Hb = Yb2-Yb1
    矩形A的中心坐標 (Xa3,Ya3) = （ (Xa2+Xa1)/2 ，(Ya2+Ya1)/2 ）
    矩形B的中心坐標 (Xb3,Yb3) = （ (Xb2+Xb1)/2 ，(Yb2+Yb1)/2 ）
同時滿足下面兩個式子，就可以說明兩個矩形相交。
1. | Xb3-Xa3 | <= Wa/2 + Wb/2 
2. | Yb3-Ya3 | <= Ha/2 + Hb/2
即：
| Xb2+Xb1-Xa2-Xa1 | <= Xa2-Xa1 + Xb2-Xb1
| Yb2+Yb1-Ya2-Ya1 | <=Y a2-Ya1 + Yb2-Yb1

## Reference 

* [判断矩形相交以及求出相交的区域](https://segmentfault.com/a/1190000006212588)   https://segmentfault.com/a/1190000006212588


###### tags: `Codility` `RaKuten` `Rectengle Area`