class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        minHeap = []
        currPassengers = 0

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                currPassengers -= heapq.heappop(minHeap)[1]
            currPassengers += numPass

            if currPassengers > capacity:
                return False
            
            heapq.heappush(minHeap, [end, numPass])
        
        return True