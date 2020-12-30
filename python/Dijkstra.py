# 入力は0-indexed
# graph = [[(1, 1), (1, 2)], [(1, 0), (1, 3)], [(1, 0), (1, 4)], [(1, 1)], [(1, 2)]]
# start = 0
#   → [0, 1, 1, 2, 2]

def dijkstra(graph, start):
    #!!!import heapq!!!
    mn = [-1] * len(graph)
    que = []
    heapq.heappush(que, (0, start))
    while len(que) > 0:
        dist, vt = heapq.heappop(que)
        if mn[vt] == -1: mn[vt] = dist
        for i, j in graph[vt]:
            if mn[j] == -1: heapq.heappush(que, (dist + i, j))
    return mn