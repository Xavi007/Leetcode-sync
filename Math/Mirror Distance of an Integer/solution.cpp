#include <cstdlib>
class Solution {
public:
    int mirrorDistance(int n) {
        int copyn = n;
        int revn = 0;

        while(n)
        {
            int digit = n % 10;
            revn = revn * 10 + digit;
            n /= 10;
        }

        return abs(revn - copyn);
    }
};