class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Use a priority queue (min-heap) to store the nodes along with their current distances
        min_heap = [(0, k)]  # (distance, node)
        min_time = {}
        
        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in min_time:
                continue

            # Record the minimum time it takes to reach this node
            min_time[node] = current_time

            # Update the distances to adjacent nodes
            for neighbor, weight in graph[node]:
                if neighbor not in min_time:
                    heapq.heappush(min_heap, (current_time + weight, neighbor))

        # If we can reach all nodes, return the maximum time; otherwise, return -1
        if len(min_time) == n:
            return max(min_time.values())
        return -1


        