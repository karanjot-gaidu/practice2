class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            l, r = i+1, len(numbers) - 1
            while l<=r:
                mid = l + (r-l)//2
                if tmp == numbers[mid]:
                    return [i+1, mid+1]
                elif tmp < numbers[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return []