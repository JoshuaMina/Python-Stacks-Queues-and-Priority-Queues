from queuesSecond import Queue

fifo = Queue("1st", "2nd", "3rd", "4th")
print(len(fifo))


for element in fifo:
    print(element)




print(len(fifo))