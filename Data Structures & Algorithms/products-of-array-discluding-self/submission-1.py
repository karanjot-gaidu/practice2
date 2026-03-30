class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for j in range(len(nums)):
            total = 1
            for i in range(len(nums)):
                if i==j:
                    continue
                total *= nums[i]
            output.append(total)
        return output
