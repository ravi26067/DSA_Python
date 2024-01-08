from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = set()
        i = 0

        while i < len(nums):
            if nums[i] not in num_set:
                num_set.add(nums[i])
                i += 1
            else:
                nums.pop(i)

        return len(nums)

    def removeDuplicatesOptimised(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0  # Slow pointer

        for j in range(1, len(nums)):  # Fast pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


