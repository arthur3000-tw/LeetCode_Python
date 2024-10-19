from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 處理邊界問題，確認座標有效性
        def valid_point(point,grid):
            i = point[0]
            j = point[1]
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

        islands = 0
        
        check_queue = deque()
        seen = set()

        m = len(grid)
        n = len(grid[0])

        # 走遍所有座標
        for i in range(m):
            for j in range(n):
                # 有無 island 的 flag
                flag = False
                # 確認座標有無看過
                if (i,j) not in seen:
                    check_queue.append((i,j))
                    seen.add((i,j))
                # 遍尋 queue
                while check_queue:
                    point = check_queue.pop()
                    value = grid[point[0]][point[1]]
                    # 確認座標位置是否為 island
                    if value == "1":
                        # 將 flag 標記為 true
                        flag = True
                        # 計算鄰近座標（上、下、左、右）
                        top = (point[0]-1,point[1])
                        down = (point[0]+1,point[1])
                        left = (point[0],point[1]-1)
                        right = (point[0],point[1]+1)
                        # 鄰近座標放入 list 中
                        arounds = [top, down, left, right]
                        # 遍尋每個鄰近座標
                        for position in arounds:
                            # 確認座標有效性及是否看過此座標
                            if valid_point(position,grid) and position not in seen:
                                check_queue.append(position)
                                seen.add(position)
                # 遍尋 queue 後，確認 flag 是否為 true
                if flag == True:
                    islands += 1

        return islands
