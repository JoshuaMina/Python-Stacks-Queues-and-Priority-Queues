from queuesSecond import Queue

fifo = Queue("1st", "2nd", "3rd", "4th")
print("Number of Current Queues:",len(fifo))


for element in fifo:
    print(element)

# The queue has three elements initially, but its length drops to zero
# after consuming all elements in a loop. Next up, you’ll implement a
# stack data type that’ll dequeue elements in reverse order.


print("Number of Current Queues:",len(fifo))