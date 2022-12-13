#In one-off scripts, you could probably get away with using a plain
# old Python list as a rudimentary stack when you don’t mind the extra
# overhead of having to copy the values from time to time:
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print(lifo)

print("The ",lifo.pop()," element has been Dequeued",lifo )

print("The ",lifo.pop()," element has been Dequeued",lifo )

print("The ",lifo.pop()," element has been Dequeued",lifo )