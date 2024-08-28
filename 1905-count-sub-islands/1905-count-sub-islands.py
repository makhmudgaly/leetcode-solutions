class Solution:
    # Directions in which we can traverse inside the grids.
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Helper method to check if the cell at the position (x, y) in the 'grid'
    # is a land cell.
    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    # Traverse all cells of island starting at position (x, y) in 'grid2',
    # and check if this island is a sub-island in 'grid1'.
    def is_sub_island(self, x, y, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])
        # Traverse on all cells using the depth-first search method.
        is_sub_island = True

        # If the current cell is not a land cell in 'grid1', then the current island can't be a sub-island.
        if not self.is_cell_land(x, y, grid1):
            is_sub_island = False

        # Traverse on all adjacent cells.
        for direction in self.directions:
            next_x = x + direction[0]
            next_y = y + direction[1]
            # If the next cell is inside 'grid2', is not visited, and is a land cell,
            # then we traverse to the next cell.
            if (
                0 <= next_x < total_rows
                and 0 <= next_y < total_cols
                and not visited[next_x][next_y]
                and self.is_cell_land(next_x, next_y, grid2)
            ):
                # Mark the next cell as visited.
                visited[next_x][next_y] = True
                next_cell_is_part_of_sub_island = self.is_sub_island(
                    next_x, next_y, grid1, grid2, visited
                )
                is_sub_island = (
                    is_sub_island and next_cell_is_part_of_sub_island
                )
        return is_sub_island

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_counts = 0

        # Iterate over each cell in 'grid2'.
        for x in range(total_rows):
            for y in range(total_cols):
                # If the cell at position (x, y) in 'grid2' is not visited,
                # is a land cell in 'grid2', and the island starting from this cell is a sub-island in 'grid1',
                # then increment the count of sub-islands.
                if not visited[x][y] and self.is_cell_land(x, y, grid2):
                    visited[x][y] = True
                    if self.is_sub_island(x, y, grid1, grid2, visited):
                        sub_island_counts += 1

        # Return total count of sub-islands.
        return sub_island_counts