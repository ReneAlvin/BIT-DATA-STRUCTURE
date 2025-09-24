from array import array

queue_counts = [25, 30, 15, 40, 28] 

total_passengers = sum(queue_counts)
average_passengers = total_passengers / len(queue_counts)
min_passengers = min(queue_counts)
max_passengers = max(queue_counts)


print("=== Dictionaries ===")


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
