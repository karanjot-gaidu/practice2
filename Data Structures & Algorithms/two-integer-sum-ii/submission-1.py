class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        for i, num in enumerate(numbers):
            if target - num in indices:
                return [indices[target-num]+1, i+1]
            indices[num] = i