class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     swapped = False
        #     for j in range(0, n - i - 1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #             swapped = True
        #     if not swapped:
        #         break
        # return nums

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])

        return result




