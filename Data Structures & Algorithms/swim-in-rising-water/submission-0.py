class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Min-heap to keep track of the current minimum elevation required to reach each cell
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, row, col)
        
        # Keep track of the visited cells
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        # Directions for moving up, down, left, and right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Track the maximum elevation we've encountered so far
        max_elevation = grid[0][0]
        
        while min_heap:
            elevation, row, col = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, elevation)
            
            # If we have reached the bottom-right corner, return the current max elevation
            if row == n - 1 and col == n - 1:
                return max_elevation
            
            # Explore the four neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))

        return -1