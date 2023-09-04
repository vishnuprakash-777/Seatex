import csv

def read_csv(filename):
    data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data


student_details = read_csv('SEAT.csv')
room_details = read_csv('roomdetails.csv')


rooms = {}
for room in room_details:
    room_number, rows, columns, benches, bench_strength = map(int, room)
    rooms[room_number] = {
        'rows': rows,
        'columns': columns,
        'benches': benches,
        'bench_strength': bench_strength,
        'students': []
    }


student_groups = {}
for status, register_no in student_details:
    if status == 'on':
        prefix = register_no[:8]  
        if prefix not in student_groups:
            student_groups[prefix] = []
        student_groups[prefix].append(register_no)


sorted_prefixes = sorted(student_groups.keys())
student_count = 0

for i, prefix in enumerate(sorted_prefixes):
    group = student_groups[prefix]
    group.sort()  
    while group:
        room_with_min_empty_seats = min(rooms, key=lambda room_num: len(rooms[room_num]['students']))
        rooms[room_with_min_empty_seats]['students'].append(group.pop(0))
        student_count += 1


for room_number, room_info in rooms.items():
    print(f"Room {room_number}:")
    for i in range(room_info['rows']):
        for j in range(room_info['columns']):
            student_index = i * room_info['columns'] + j
            if student_index < len(room_info['students']):
                print(room_info['students'][student_index], end="\t")
            else:
                print("Empty", end="\t")
        print()
    print()

print(f"Total students assigned: {student_count}")

