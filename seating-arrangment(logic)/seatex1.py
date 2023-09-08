from random import shuffle
from pprint import pprint as printf
from os import system
import numpy as np
#shuffling correct

number_of_row_in_room = int(input('Enter Number of Rows Room :'))
number_of_col_in_room = int(input('Enter Number of Columns Room :'))

system('color 1')

number_of_Student_in_room = number_of_row_in_room * number_of_col_in_room

register_data = []

while True:
    register_prefix = input('Enter Register Number Prefix (e.g., "NA20PICS") or "q" to quit: ')
    if register_prefix == "q":
        break

    starting_Register = int(input('Enter Starting Register Number :'))
    ending_Register = int(input('Enter Last Register Number :'))

    # Generate register numbers with the specified prefix and sequential order
    Register_List = [f'{register_prefix}{i:02}' for i in range(starting_Register, ending_Register + 1)]
    register_data.extend(Register_List)

# Shuffle the students randomly
shuffle(register_data)

# Create a dictionary to group students by prefix
students_by_prefix = {}
for student in register_data:
    prefix = student[:2]
    if prefix not in students_by_prefix:
        students_by_prefix[prefix] = []
    students_by_prefix[prefix].append(student)

# Create a list to store the final seating plan
seatingPlan = []

# Generate sequential orders for each prefix
for prefix, students in students_by_prefix.items():
    sequential_order = [f'{prefix}{i:02}' for i in range(1, len(students) + 1)]
    shuffle(sequential_order)
    students_by_prefix[prefix] = sequential_order

# Arrange students ensuring no same-prefix students are adjacent
while any(students_by_prefix.values()):
    for prefix in students_by_prefix.keys():
        if students_by_prefix[prefix]:
            student = students_by_prefix[prefix].pop(0)
            seatingPlan.append(student)

x, y, z = 1, number_of_row_in_room, number_of_col_in_room

# Fill any remaining seats with '0'
seatingPlan += ['0' for _ in range(number_of_Student_in_room - len(seatingPlan))]

arr = np.array(seatingPlan, dtype=str).reshape((x, y, z))

print("\nSeating Plan for All Students in a Single Room:\n")
printf(arr)
