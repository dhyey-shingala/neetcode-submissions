class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []
        for i in nums:
            if i not in nums_list:
                nums_list.append(i)
            else:
                return True
        return False