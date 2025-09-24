from array import array

queue_counts = [25, 30, 15, 40, 28] 

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)


print(f"Total passengers: {total_passengers}")
print(f"Average passengers per queue: {average_passengers:.2f}")
print(f"Minimum passengers in a queue: {min_passengers}")
print(f"Maximum passengers in a queue: {max_passengers}")
print()
