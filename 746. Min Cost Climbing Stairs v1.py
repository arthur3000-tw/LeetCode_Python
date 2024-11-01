class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_length = len(cost)
        ans = [0] * (cost_length +1)
        for i in range(2,cost_length+1):
            ans[i] = min(ans[i-2]+cost[i-2], ans[i-1]+cost[i-1])
        return ans[cost_length]
