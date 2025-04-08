import heapq
heap = []
heapq.heappush(heap, ('V', 1))
heapq.heappush(heap, ('V', 2))
heapq.heappush(heap, ('V', 3))
for a in heap:
	print(a)