from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid_point(point,grid):
            i = point[0]
            j = point[1]
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        islands = 0
        
        check_queue = deque()
        seen = set()

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                flag = False
                if (i,j) not in seen:
                    check_queue.append((i,j))
                    seen.add((i,j))
                while check_queue:
                    point = check_queue.pop()
                    value = grid[point[0]][point[1]]
                    if value == "1":
                        flag = True
                        # arounds
                        top = (point[0]-1,point[1])
                        down = (point[0]+1,point[1])
                        left = (point[0],point[1]-1)
                        right = (point[0],point[1]+1)
                        arounds = [top, down, left, right]
                        for position in arounds:
                            if valid_point(position,grid) and position not in seen:
                                check_queue.append(position)
                                seen.add(position)
                if flag == True:
                    islands += 1

        return islands
