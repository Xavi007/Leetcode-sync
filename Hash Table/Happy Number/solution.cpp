#include <unordered_set>
using namespace std;

class Solution {
public:

    int power(int base, int exp) {
        int result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }

    int digitSquareSum(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += power(digit, 2); 
            n /= 10;
        }
        return sum;
    }

    bool isHappy(int n) {
        unordered_set<int> seen;   

        while (n != 1 && seen.count(n) == 0) {
            seen.insert(n);
            n = digitSquareSum(n);
        }

        return n == 1;
    }
};