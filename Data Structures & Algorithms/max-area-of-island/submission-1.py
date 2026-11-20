#go through the matrix, find the max number of 1s touching, so using dfs (depth first search)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitedcoord = set()
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) in visitedcoord:
                    continue
                area = self.dfs(grid, visitedcoord, i, j)   # 0 for water, island size for land
                if area > maxarea:
                    maxarea = area
        return maxarea

    def dfs(self, grid, visitedcoord, i, j):
        # stop if off the grid, on water, or already counted
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0 or (i, j) in visitedcoord:
            return 0
        visitedcoord.add((i, j))   # the same set everywhere, no need to return it
        # separate calls (not elif), so every direction is explored, and the areas are added up
        return (1 + self.dfs(grid, visitedcoord, i, j + 1)
                  + self.dfs(grid, visitedcoord, i + 1, j)
                  + self.dfs(grid, visitedcoord, i, j - 1)
                  + self.dfs(grid, visitedcoord, i - 1, j))