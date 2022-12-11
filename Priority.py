from heapq import heappush, heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print("The list of Queue",fruits)

heappop(fruits)


print("The list of Queue",fruits)
#When you pop an element from a heap, you’ll always get the first one,
# while the remaining elements might shuffle a little bit