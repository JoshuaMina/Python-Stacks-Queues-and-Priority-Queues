from queues import Queue
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
fifo.enqueue("4th")

fifo.dequeue()

fifo.dequeue()

fifo.dequeue()

