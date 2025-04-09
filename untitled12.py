#from top to bottom
from functools import lru_cache
from typing import List
class Solution:
    def maxArea(self, n: int, cuts: List[int]) -> int:
        def cut(curlength):
            if curlength==0:
                return 0
            q=0
            for i in range(1,curlength+1):
                q=max(q,cuts[i-1]+cut(curlength-i))
            return q
        return cut(n)
solution = Solution()
n = 4  # 钢条长度
cuts = [1,5,8,9,10]  # 每个长度的收益
print(solution.maxArea(n, cuts)) 
            
                
        