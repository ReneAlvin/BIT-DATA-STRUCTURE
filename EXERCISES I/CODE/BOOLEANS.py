from array import array

queue_counts = [25, 30, 15, 40, 28] 

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)

print("=== Booleans ===")
threshold = 25

if average_passengers > threshold and max_passengers > 35:
    print("Above Standard")
else:
    print("Below Standard")
print()
