class Solution {
public:

    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; 1LL * i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    int countPrimeSetBits(int left, int right) {
        int ans = 0;

        for (int x = left; x <= right; x++) {
            int cnt = __builtin_popcount(x);   
            if (isPrime(cnt)) ans++;
        }

        return ans;
    }
};