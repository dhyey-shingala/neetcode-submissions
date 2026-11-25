class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = numbers[i]
            for j in range(len(numbers)):
                if x + numbers[j] == target:
                    return [i+1, j+1]