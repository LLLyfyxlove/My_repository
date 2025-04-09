from functools import lru_cache
from typing import List

class Solution:
    def maxArea(self, n: int, cuts: List[int]) -> int:
        # 初始化 dp 数组，dp[i] 表示长度为 i 的钢条的最大收益
        dp = [float('-inf')] * (n + 1)
        where=[0]*n
        dp[0] = 0
        
        # 递归函数，计算长度为 curLength 的钢条的最大收益
        @lru_cache(None)
        def cut(curLength: int) -> int:
            if curLength == 0:
                return 0
            if dp[curLength] != float('-inf'):
                return dp[curLength]
            max_revenue = 0
            for i in range(1, curLength + 1):
                if max_revenue<cuts[i - 1] + cut(curLength - i):
                    max_revenue = max(max_revenue, cuts[i - 1] + cut(curLength - i))
                    where[j-1]=where[i-1]+1
            dp[curLength] = max_revenue
            return dp[curLength]
        
        # 从最长的钢条开始递归计算最大收益
        cut(n)
        return dp[n]

solution = Solution()
n = 4  # 钢条长度
cuts = [ 1, 5, 8, 9, 10]  # 每个长度的收益，添加0代表长度为1的收益
print(solution.maxArea(n, cuts))  # 输出：最大收益