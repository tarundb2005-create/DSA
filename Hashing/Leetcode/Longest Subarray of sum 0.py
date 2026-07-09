#geeksforgeeks
class Solution:
    def maxLength(self, arr):
        # code here
        prefix = 0
        longest = 0
        hashmap = {}
        for i in range(len(arr)):
            prefix += arr[i]
            if prefix == 0:
                longest = i + 1
            if prefix in hashmap:
                longest = max(longest , i - hashmap[prefix])
            else:
                hashmap[prefix] = i
        return longest
