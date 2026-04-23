class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        for i in range(len(trips)):
            currPassengers = trips[i][0]
            for j in range(i):
                if trips[j][2] > trips[i][1]:
                    currPassengers += trips[j][0]
            if currPassengers > capacity:
                return False
        return True