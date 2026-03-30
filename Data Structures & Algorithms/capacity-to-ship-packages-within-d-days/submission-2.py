class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res