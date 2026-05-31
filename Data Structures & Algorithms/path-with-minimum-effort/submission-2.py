class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(limit):
            stack = [(0, 0)]
            visited = {(0, 0)}

            while stack:
                r, c = stack.pop()

                if r == ROWS - 1 and c == COLS - 1:
                    return True

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (
                        row < 0 or col < 0 or
                        row >= ROWS or col >= COLS or
                        (row, col) in visited or
                        abs(heights[row][col] - heights[r][c]) > limit
                    ):
                        continue

                    visited.add((row, col))
                    stack.append((row, col))

            return False
        
        l, r = 0, 1000000
        res = r

        while l <= r:
            mid = (l + r) // 2
            if dfs(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res