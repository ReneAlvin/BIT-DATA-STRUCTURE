from array import array

queue_counts = [25, 30, 15, 40, 28]  

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)


print("=== Strings ===")
report = (
    f"Flight Check-in Report:\n"
    f"Total Passengers: {total_passengers}\n"
    f"Average per Queue: {average_passengers:.2f}"
)
print(report)

summary = f"Queues: {len(queue_counts)}, Min: {min_passengers}, Max: {max_passengers}"
print(summary)
print()
