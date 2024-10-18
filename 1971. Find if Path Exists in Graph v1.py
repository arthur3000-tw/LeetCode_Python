class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # 當目標點與起始點相同
        if source == destination:
            return True
        
        graph = defaultdict(list)
        check_queue = deque([source])
        seen = set()

        # 建立 graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 遍尋 queue 中所元素
        while check_queue:
            # 從 queue 中取出第一個元素
            point = check_queue.popleft()
            # 確認此點是否為目標點
            if point == destination:
                return True
            else:
                # 不是目標點時，取得此點鄰居
                for neighbor in graph[point]:
                    # 若此鄰居沒有看過，將此鄰居放入 queue 中，並且加入已看過的 set 中
                    if neighbor not in seen:
                        seen.add(neighbor)
                        check_queue.append(neighbor)

        return False
        # Time O(V + E)
        # Space O(V + E)
