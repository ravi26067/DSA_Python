from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i, num in enumerate(nums):
            complmnt = target - num

            if complmnt in my_map:
                return [my_map[complmnt], i]

            my_map[num] = i

        return []


# Example usage
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print("Output:", result)
