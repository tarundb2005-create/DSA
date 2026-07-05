#WITH NO TARGET
#LEETCODE VERSION USING HELPER FUNCTION DFS
#USING COPY FOR THE ANS TO RESULT 
class Solution:
    def subset(self,nums):
        nums.sort()
        result = []
        def dfs(index,ans):
            result.append(ans.copy())
            for i in range(index,len(nums)):
                if i > index and nums[i] == nums [i - 1]:
                    continue
                ans.append(nums[i])
                dfs(i + 1,ans)
                ans.pop()
        dfs(0,[])
        return result
