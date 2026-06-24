class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            cal = 0
            for  p in piles:
                cal += (p + k - 1) // k
            if cal <= h:
                res = min(res,k)
                right = k -1 
            else:
                left = k + 1
        return res
            
        
