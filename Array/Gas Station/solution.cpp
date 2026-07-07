class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int gas_total = 0;
        int cost_total = 0;
        int tank = 0;
        int length = gas.size();
        int start_idx = 0;

        for(int idx = 0; idx < length; ++idx)
        {
            gas_total += gas[idx]; // 4, 9, 10, 12, 15
            cost_total += cost[idx]; // 1, 3, 6, 10, 15

            tank += gas[idx] - cost[idx]; // 3, 6, 4, 2, 0

            if (tank < 0)
            {
                start_idx = idx+1;
                tank = 0;
            }
        }

        printf("%d", gas_total);
        printf("\n%d", cost_total);

        if (gas_total >= cost_total)
        {
            return start_idx;
        }
        else
        {
            return -1;
        }
    }
};