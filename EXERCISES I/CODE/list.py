from array import array

queue_counts = [25, 30, 15, 40, 28] 

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)


passenger_names = ["Alice", "Bob", "Charlie", "Diana"]
print("Original list:", passenger_names)

passenger_names.append("Ethan")

for name in passenger_names:
    if name.startswith("C"):
        passenger_names.remove(name)
        break

passenger_names.sort()
print("Modified & Sorted list:", passenger_names)
print()
