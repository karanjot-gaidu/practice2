class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        for num in nums:
            val = abs(num)
            if val > 0 and val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -(n+1)
        for i in range(n):
            if nums[i] >= 0:
                return i+1
        return n + 1