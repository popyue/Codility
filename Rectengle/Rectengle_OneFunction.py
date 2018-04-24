# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 3.6
    '''
    K,L,M,N ： 第一個矩形 (K,L)(M,N)
    P,Q,R,S ： 第二個矩形 (P,Q)(R,S)
    '''
    #Initialization
    result=0
    length1=0   #First Rectengle 長
    width1=0    #First Rectengle 寬
    firstrec=0  #First Rectengle 面積
    length2=0   #Second Rectengle 長
    width2=0    #Second Rectengle 寬
    secondrec=0 #Second Rectengle 面積
    
    #計算 First Rectengle 長,寬,面積
    length1=abs(K-M)
    width1=abs(L-N)
    firstrec=length1*width1
    
    #Second Rectengle 長,寬,面積
    length2=abs(P-R)
    width2=abs(Q-S)
    secondrec=length2*width2
    
    #First Rectengle Center 第一個矩形的中心座標 
    firstcentX=(K+M)/2
    firstcentY=(L+N)/2

    #Second Rectengle Center 第二個矩形的中心座標
    secondcentX=(P+R)/2
    secondcentY=(Q+S)/2

    # Intersect area 相交的區域
    # 判斷是否相交
    if abs(secondcentX-firstcentX) <= length1/2+length2/2 and abs(secondcentY-firstcentY) <= width1/2+width2/2:
        #計算相交的矩形之對角的座標
        thirdrectX1=max(K,P)
        thirdrectY1=max(L,Q)
        thirdrectX2=min(M,R)
        thirdrectY2=min(N,S)
        # 計算相交矩形面積
        thirdrec=abs((thirdrectX1-thirdrectX2)*(thirdrectY1-thirdrectY2))
        #計算結果
        result=firstrec+secondrec-thirdrec
        if result >=2147483647:
            return -1
        else:
            print result
            return result
    else:
        result=firstrec+secondrec
        if result >=2147483647:
            return -1
        else:
            print '2'
            print result
            return result
if __name__ == '__main__':
    solution(-4,1,2,6,0,-1,4,3)