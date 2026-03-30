class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    min_len = min(min_len, j-i+1)
                    break
        return min_len if min_len != float('inf') else 0