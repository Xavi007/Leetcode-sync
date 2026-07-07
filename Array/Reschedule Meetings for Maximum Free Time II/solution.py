class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        q=[]
        l=[]
        prevEnd=0
        n=len(startTime)
        for a,b in zip(startTime,endTime):
            q.append(a-prevEnd) 
            l.append(b-a)       
            prevEnd=b
        q.append(eventTime-prevEnd)
        answ=max(q)
        h=sorted(q) 
        for i in range(n):
            j=1+n-bisect.bisect_left(h,l[i])
            if l[i]<=q[i]: j-=1
            if l[i]<=q[i+1]: j-=1
            if 0<j:
                answ=max(answ,q[i]+q[i+1]+l[i])
            elif j==0:
                answ=max(answ,q[i]+q[i+1])     
        return answ