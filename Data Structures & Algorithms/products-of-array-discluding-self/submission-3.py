class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod, zero_cnt = 1, 0
        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_cnt += 1
        # if zero_cnt > 1: return [0] * len(nums)

        # result = [0] * len(nums)
        # for i,c in enumerate(nums):
        #     if zero_cnt: result[i] = 0 if c else prod
        #     else:
        #         result[i] = prod // c
        # return result

        n = len(nums)
        result = [0]*n
        prefix = [0]*n
        suffix = [0]*n

        prefix[0] = suffix[n-1] = 1
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result

