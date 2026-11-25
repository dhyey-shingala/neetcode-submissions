class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = sorted(set(nums))

        longest_seq = 1 
        current_seq = 1

        for i in range(1, len(unique_nums)):
            if unique_nums[i] - unique_nums[i - 1] == 1:
                current_seq += 1
                longest_seq = max(longest_seq, current_seq)
            else:
                current_seq = 1

        return longest_seq