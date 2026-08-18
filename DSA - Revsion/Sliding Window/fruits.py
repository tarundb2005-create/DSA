def Fruits(nums):
  l = 0
  count = {}
  res = 0

  for r in range(len(nums)):

      count[nums[r]] = count.get(nums[r], 0) + 1

      while len(count) > 2:

          count[nums[l]] -= 1

          if count[nums[l]] == 0:
              del count[nums[l]]

          l += 1

      res = max(res, r - l + 1)

  return res
