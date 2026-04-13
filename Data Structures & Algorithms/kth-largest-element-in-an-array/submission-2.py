class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        while k:
            num = heapq.heappop(maxHeap)
            k -= 1
        
        return -num