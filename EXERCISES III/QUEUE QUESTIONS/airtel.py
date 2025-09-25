from collections import deque

# Step 1: 4 customers join the queue
queue = deque(["Customer1", "Customer2", "Customer3", "Customer4"])
print("Initial Queue:", queue)

# Step 2: In FIFO, the last served is the last in the queue
last_served = queue[-1]  # get the last element
print("Last customer to be served:", last_served)
