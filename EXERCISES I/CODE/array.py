from array import array

queue_counts = [25, 30, 15, 40, 28] 

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)

print("=== Arrays ===")


queue_array = array('i', queue_counts)
sum_array = sum(queue_array)
print("Sum from list:", total_passengers)
print("Sum from array:", sum_array)
print()