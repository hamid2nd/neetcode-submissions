class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()            # empty set. visited.add((i, j)) marks cell (i, j) as visited. (i, j) in visited retuns True/False depending if a coordinate has been visited or not
        #need a function that checks above, left, right and below column for land, it has be recursive (called again automatically if land found) 
        #need to somehow note which nodes have been noted as land as well - can do this in a hash map 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited: #need to add 2nd cond - and is not in visited vertices
                    visited.add((i, j))                    #note this node in visited
                    self.connectedland(i, j, visited, grid) #call recursive search for connected land, send it current pos as well as visited to be updated with more vertices. 
                    islands += 1
        return islands 

    def connectedland(self, i, j, visited, grid):
        if i - 1 >= 0 and grid[i-1][j] == "1" and (i-1, j) not in visited:
            visited.add((i-1, j))
            self.connectedland(i-1, j, visited, grid)
        if i + 1 < len(grid) and grid[i+1][j] == "1" and (i+1, j) not in visited:
            visited.add((i+1, j))
            self.connectedland(i+1, j, visited, grid)
        if j - 1 >= 0 and grid[i][j-1] == "1" and (i, j-1) not in visited:
            visited.add((i, j-1))
            self.connectedland(i, j-1, visited, grid)
        if j + 1 < len(grid[i]) and grid[i][j+1] == "1" and (i, j+1) not in visited:
            visited.add((i, j+1))
            self.connectedland(i, j+1, visited, grid)
#note don't need to return visited as a set is mutable so changes to visited here changes globally
