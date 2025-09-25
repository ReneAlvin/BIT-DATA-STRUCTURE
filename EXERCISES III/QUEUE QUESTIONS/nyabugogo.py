from collections import deque

queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5", "Bus6", "Bus7", "Bus8", "Bus9"])
print("Initial Queue:", queue)

for _ in range(5):
    departed = queue.popleft() 
    print("Departed:", departed)

front_bus = queue[0]  
print("Bus now in front:", front_bus)
