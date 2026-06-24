class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            capacity = (left + right) // 2

            days_needed = 1
            current_weight = 0

            for w in weights:
                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = w
                else:
                    current_weight += w

            if days_needed <= days:
                right = capacity
            else:
                left = capacity + 1

        return left
