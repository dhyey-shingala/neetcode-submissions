from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            ans.append(prod(nums[:i] + nums[i+1:]))
        return ans