#include <stdio.h>
#include <limits.h>

int getLargestOutlier(int* v, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += v[i];
    }

    int m = INT_MIN;
    int maxVal = 2000;  // We know nums[i] <= 1000, so range from -1000 to 1000.
    int freq[2001] = {0};  // Frequency array to track counts of numbers, offset by +1000.

    // Populate frequency array
    for (int i = 0; i < n; i++) {
        freq[v[i] + 1000]++;
    }

    // Try to find the largest outlier
    for (int i = 0; i < n; i++) {
        int k = v[i];
        if ((sum - k) % 2 == 0) {
            int p = (sum - k) / 2;
            // Check if 'p' exists in the array and is not the same as 'k'
            if (p != k) {
                if (p + 1000 >= 0 && p + 1000 <= maxVal && freq[p + 1000] > 0) {
                    m = (m > k) ? m : k;
                }
            } else {
                // If 'p == k', check if it appears more than once
                if (freq[p + 1000] > 1) {
                    m = (m > k) ? m : k;
                }
            }
        }
    }

    return m;
}
