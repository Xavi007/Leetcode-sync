class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        start_idx = 0
        gas_total = 0
        cost_total = 0
        tank = 0

        for i in range(length):
            gas_total += gas[i]
            cost_total += cost[i]

            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start_idx = i + 1

        return start_idx if gas_total >= cost_total else -1 

                