class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        directions = ((0,1), (1,0), (-1, 0), (0, -1))
        n = len(grid)

        group = 1

        # color -> size
        sizes = dict()

        # DFS recursive func to color an island
        def color(i, j, group):
            grid[i][j] = group
            sizes[group] += 1
            for d in directions:
                _i, _j = i+d[0], j+d[1]
                if 0<=_i<n and 0<=_j<n and grid[_i][_j] == 1:
                    color(_i, _j, group)


        # we color each separate island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    group += 1
                    sizes[group] = 0
                    color(i, j, group)


        # case with only 0s
        if len(sizes)==0:
            return 1
        

        visited = [1, 1, 1, 1]
        max_size = 0

        # we do another pass looking for 0s
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
                    # we store already visited colors to avoid duplicates islands
                    visited[0], visited[1], visited[2], visited[3] = 1, 1, 1, 1
                    for k, d in enumerate(directions):
                        _i, _j = i+d[0], j+d[1]
                        if 0<=_i<n and 0<=_j<n:
                            group = grid[_i][_j] 
                            if group != 0 and group not in visited:
                                visited[k] = group
                                # if color has not been visited before, we include its size to the total
                                size += sizes[group]
                    # we check if changing that 0 to a 1 would be the best solution until now
                    max_size = max(size, max_size)

        # result is either max_size, either the biggest island (case with only 1s)
        return max(max_size, max(sizes.values()))


                    
        