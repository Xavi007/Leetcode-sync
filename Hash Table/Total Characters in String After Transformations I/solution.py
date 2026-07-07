class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        cnt = Counter(s)
        que = deque(cnt[ch] for ch in letters)    

        for _ in range(t):
            que.appendleft(que.pop())
            que[1] += que[0]
        
        return sum(que) % (10**9 + 7)
        