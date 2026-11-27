from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = time

            for nei, w in graph[node]:
                heapq.heappush(heap, (time + w, nei))

        return max(dist.values()) if len(dist) == n else -1        