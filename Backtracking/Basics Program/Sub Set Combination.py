class Solution:
    def permute(self,nums):
        result = []
        def dfs(index):
        
            if index == len(nums):
                result.append(nums.copy())
                return
            for i in range(index , len(nums)):
                nums[index],nums[i] = nums[i],nums[index]
                dfs(index + 1)
                nums[index],nums[i] = nums[i],nums[index]
        dfs(0)
        return result 
            
nums = [1,2,3]
obj = Solution()
answer = obj.permute(nums)
for permutation in answer:
    print(permutation)
