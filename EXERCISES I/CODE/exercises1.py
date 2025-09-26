from array import array

queue_counts = [25, 30, 15, 40, 28]  

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)

print(" Integers")
print(f"Total passengers: {total_passengers}")
print(f"Average passengers per queue: {average_passengers:.2f}")
print(f"Minimum passengers in a queue: {min_passengers}")
print(f"Maximum passengers in a queue: {max_passengers}")
print()

print(" Strings ")
report = (
    f"Flight Check-in Report:\n"
    f"Total Passengers: {total_passengers}\n"
    f"Average per Queue: {average_passengers:.2f}"
)
print(report)

summary = f"Queues: {len(queue_counts)}, Min: {min_passengers}, Max: {max_passengers}"
print(summary)
print()

print(" Booleans ")
threshold = 25

if average_passengers > threshold and max_passengers > 35:
    print("Above Standard")
else:
    print("Below Standard")
print()

print(" Lists")

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

print(" Arrays ")
queue_array = array('i', queue_counts)
sum_array = sum(queue_array)
print("Sum from list:", total_passengers)
print("Sum from array:", sum_array)
print()

print(" Dictionaries ")
records = [
    {'id': 1, 'name': 'Alice', 'value': 25},
    {'id': 2, 'name': 'Bob', 'value': 30},
    {'id': 3, 'name': 'Diana', 'value': 28}
]

for record in records:
    if record['name'] == 'Bob':
        record['value'] = 35

records = [r for r in records if r['name'] != 'Diana']

total_value = sum(r['value'] for r in records)

print("Records after update & delete:", records)
print("Total 'value' across records:", total_value)
