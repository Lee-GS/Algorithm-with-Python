from collections import deque

def bfs(start, graph, n):
    distances = [-1] * (n + 1)
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    return distances

def find_kevin_bacon_user(n, friendships):
    graph = [[] for _ in range(n + 1)]
    
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)
    
    min_kevin_bacon = float('inf')
    min_user = -1
    
    for i in range(1, n + 1):
        distances = bfs(i, graph, n)
        kevin_bacon_number = sum(dist for dist in distances[1:] if dist != -1)
        
        if kevin_bacon_number < min_kevin_bacon:
            min_kevin_bacon = kevin_bacon_number
            min_user = i
    
    return min_user

# 입력 받기
n, m = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(m)]

# 케빈 베이컨의 수가 가장 작은 사람 찾기
result = find_kevin_bacon_user(n, friendships)
print(result)
