class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        graph = defaultdict(list)
        check_queue = deque([source])
        seen = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while check_queue:
            point = check_queue.popleft()
            if point == destination:
                return True
            else:
                for neighbor in graph[point]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        check_queue.append(neighbor)

        return False
