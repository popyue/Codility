# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#First Rectengle length, width
def RectAinfo(K,L,M,N):
    infoA=[]
    lengthA=abs(K-M)
    infoA.append(lengthA)
    widthA=abs(L-N)
    infoA.append(widthA)
    return infoA
#Second Rectengle length, width
def RectBinfo(P,Q,R,S):
    infoB=[]
    lengthB=abs(P-R)
    infoB.append(lengthB)
    widthB=abs(Q-S)
    infoB.append(widthB)
    return infoB

# Rectengle1 information
def AreaA(K,L,M,N):
    rectA=RectAinfo(K,L,M,N)
    lengthA=rectA[0]
    widthA=rectA[1]
    firstarea=lengthA*widthA
    return firstarea

#First Rectengle Center
def CenterPointA(K,L,M,N):
    FirstCent=[]
    firstcentX=(K+M)/2
    FirstCent.append(firstcentX)
    firstcentY=(L+N)/2
    FirstCent.append(firstcentY)
    return FirstCent 

# Rectengle2 information    
def AreaB(P,Q,R,S):
    rectB=RectBinfo(P,Q,R,S)
    lengthB=rectB[0]
    widthB=rectB[1]
    secondarea=lengthB*widthB        
    return secondarea

#Second Rectengle Center
def CenterPointB(P,Q,R,S):
    SecondCent=[]
    secondcentX=(P+R)/2
    SecondCent.append(secondcentX)
    secondcentY=(Q+S)/2
    SecondCent.append(secondcentY)
    return SecondCent

#判斷重疊
def Intersectornot(K,L,M,N,P,Q,R,S):
    RectengleA=RectAinfo(K,L,M,N)
    RectengleB=RectBinfo(P,Q,R,S)
    CenterA=CenterPointA(K,L,M,N)
    CenterB=CenterPointB(P,Q,R,S)
    if abs(CenterB[0]-CenterA[0]) <= RectengleA[0]/2+RectengleB[0]/2 and abs(CenterB[1]-CenterA[1]) <= RectengleA[1]/2+RectengleB[1]/2:
        return True
    else:
        return False

def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 3.6
    #Initialization
    result=0
    areaA=AreaA(K,L,M,N)
    areaB=AreaB(P,Q,R,S)
    # Intersect area
    if Intersectornot(K, L, M, N, P, Q, R, S)== True:
        thirdrectX1=max(K,P)
        #print thirdrectX1
        thirdrectY1=max(L,Q)
        #print thirdrectY1
        thirdrectX2=min(M,R)
        #print thirdrectX2
        thirdrectY2=min(N,S)
        #print thirdrectY2
        AreaC=abs((thirdrectX1-thirdrectX2)*(thirdrectY1-thirdrectY2))
        #print AreaC
        result=areaA+areaB-AreaC
        if result >=2147483647:
            return -1
        else:
            #print '1'
            print result
            return result
    else:
        result=areaA+areaB
        if result >=2147483647:
            return -1
        else:
            #print '2'
            print result
            return result
        
if __name__ == '__main__':  
    solution(-4,1,2,6,0,-1,4,3)