def solution(n, wires):
    answer = 10e9
    
    def dfs(v,graph):
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == 0:
                dfs(i,graph)
                
    def solution2(arr,wire):
        arr[wire[0]].remove(wire[1])
        arr[wire[1]].remove(wire[0])
        #print(arr)
        dfs(1,arr)
        cnt = abs(visited.count(1)-(visited.count(0)-1))
        return cnt
                
    for j in range(len(wires)):
        graph=[[] for _ in range(n+1)]
        for i in range(len(wires)):
            graph[wires[i][0]].append(wires[i][1])
            graph[wires[i][1]].append(wires[i][0])
        print(graph)
        visited=[0]*(n+1)
        count = solution2(graph,wires[j])
        answer = min(count,answer)
        
        
    return answer