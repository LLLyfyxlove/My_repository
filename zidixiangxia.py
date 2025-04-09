from functools import lru_cache
from typing import List

class Solution:
    def maxArea(self, n: int, cuts: List[int]) -> int:
        # 初始化 dp 数组，dp[i] 表示长度为 i 的钢条的最大收益
        dp = [0] * (n+1)
        where=[0]*n
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]=max(dp[i],cuts[j-1]+dp[i-j])
        # 从最长的钢条开始递归计算最大收益
        return dp[-1]

solution = Solution()
n = 4  # 钢条长度
cuts = [ 1, 5, 8, 9, 10]  # 每个长度的收益，添加0代表长度为1的收益
print(solution.maxArea(n, cuts))  # 输出：最大收益