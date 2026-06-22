class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
      left = 0
      min_a = float ("inf")
      curr = 0
      for right in range(len(nums)):
        curr += nums[right]
        while curr >= target:
          min_a = min(min_a , right - left + 1)
          curr -= nums[left]
          left += 1
      return 0 if min_a == float("inf") else min_a
