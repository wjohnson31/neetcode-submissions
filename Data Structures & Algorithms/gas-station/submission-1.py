class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        costs = []
        for i in range(len(gas)):
            costs.append(gas[i] - cost[i])
        if sum(costs) < 0:
            return -1
        start = 0
        tank = 0
        for i in range(len(costs)):
            tank += costs[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start