class Solution:
    def primeSubarray(self, arr, limit_gap):
        n = len(arr)
        max_val = max(arr)
        prime_flag = [True] * (max_val + 1)
        prime_flag[0] = prime_flag[1] = False

        for i in range(2, int(max_val**0.5) + 1):
            if prime_flag[i]:
                for j in range(i * i, max_val + 1, i):
                    prime_flag[j] = False

        prime_pos = []
        prime_vals = []
        for idx, num in enumerate(arr):
            if prime_flag[num]:
                prime_pos.append(idx)
                prime_vals.append(num)

        m = len(prime_pos)
        if m < 2:
            return 0

        jump = [0] * m
        acc = [0] * m
        for i in range(m):
            nxt = prime_pos[i + 1] if i + 1 < m else n
            jump[i] = nxt - prime_pos[i]
            acc[i] = jump[i] + (acc[i - 1] if i > 0 else 0)

        res = 0
        min_q = []
        max_q = []
        r_ptr = 0

        for l_ptr in range(m):
            while r_ptr < m:
                val = prime_vals[r_ptr]

                while min_q and prime_vals[min_q[-1]] > val:
                    min_q.pop()
                min_q.append(r_ptr)

                while max_q and prime_vals[max_q[-1]] < val:
                    max_q.pop()
                max_q.append(r_ptr)

                low = prime_vals[min_q[0]]
                high = prime_vals[max_q[0]]

                if high - low <= limit_gap:
                    r_ptr += 1
                else:
                    if min_q and min_q[-1] == r_ptr:
                        min_q.pop()
                    if max_q and max_q[-1] == r_ptr:
                        max_q.pop()
                    break

            rightmost = r_ptr - 1
            if rightmost >= l_ptr + 1:
                left_len = prime_pos[l_ptr] - (prime_pos[l_ptr - 1] if l_ptr else -1)
                right_sum = acc[rightmost] - acc[l_ptr]
                res += left_len * right_sum

            if min_q and min_q[0] == l_ptr:
                min_q.pop(0)
            if max_q and max_q[0] == l_ptr:
                max_q.pop(0)

        return res