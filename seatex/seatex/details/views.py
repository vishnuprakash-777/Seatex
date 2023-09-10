from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CSVUploadForm
from .models import Details,RoomDetails
import csv
import io

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_csv_file(request.FILES['csv_file'])
            messages.success(request, "CSV file uploaded successfully.")
            return redirect('admin:details_details_changelist')
    else:
        form = CSVUploadForm()
    return render(request, 'admin/upload_csv.html', {'form': form})

def handle_csv_file(self, csv_file):
    csv_data = csv_file.read().decode('utf-8')
    reader = csv.reader(io.StringIO(csv_data))

    for row in reader:
        status = row[0]  # Assuming the status is in the first column
        reg_no = row[1]  # Assuming the RegNo is in the second column

        details = Details(status=status, RegNo=reg_no)
        details.save()




import pandas as pd
from django.http import HttpResponse
import numpy as np

def generate_seating_plan(request):
    if request.method == 'POST':
        roomno = request.POST.get('roomno')

        # Fetch room details from the database
        room = RoomDetails.objects.get(roomno=roomno)
        number_of_row_in_room = room.rows
        number_of_col_in_room = room.columns

        # Fetch student register numbers from the database
        register_data = Details.objects.values_list('RegNo', flat=True).distinct()

        # Calculate the maximum number of students the room can accommodate
        max_students = number_of_row_in_room * number_of_col_in_room

        if len(register_data) > max_students:
            # Students strength exceeds room size, return a custom response
            return render(request, 'students_strength_exceeds.html')
        else:
            # Create a dictionary to group students by prefix
            students_by_prefix = {}
            for student in register_data:
                prefix = student[:8]
                if prefix not in students_by_prefix:
                    students_by_prefix[prefix] = []
                students_by_prefix[prefix].append(student)

            # Create a list to store the final seating plan
            seatingPlan = []

            # Generate sequential orders for each prefix
            for prefix, students in students_by_prefix.items():
                sequential_order = [f'{prefix}{i:02}' for i in range(1, len(students) + 1)]
                students_by_prefix[prefix] = sequential_order

            # Arrange students ensuring no same-prefix students are adjacent
            while any(students_by_prefix.values()):
                for prefix in students_by_prefix.keys():
                    if students_by_prefix[prefix]:
                        student = students_by_prefix[prefix].pop(0)
                        seatingPlan.append(student)

            x, y, z = 1, number_of_row_in_room, number_of_col_in_room

            # Fill any remaining seats with '0'
            seatingPlan += ['0' for _ in range(number_of_row_in_room * number_of_col_in_room - len(seatingPlan))]

            arr = np.array(seatingPlan, dtype=str).reshape((x, y, z))

            # Convert seating plan data to a DataFrame
            df = pd.DataFrame(arr[0])

            # Create a header row with the room number
            header = pd.DataFrame([['ROOM NO', roomno]])

            # Combine the header with the seating plan data
            df = pd.concat([header, df])

            # Create an Excel response
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = f'attachment; filename="seating_plan_{roomno}.xlsx"'

            # Write DataFrame to Excel
            df.to_excel(response, index=False, header=False)

            return response
    else:
        return render(request, 'room_selection.html')




'''
def generate_seating_plan2(request):
    if request.method == 'POST':
        roomno = request.POST.get('roomno')

        # Fetch room details from the database
        room = RoomDetails.objects.get(roomno=roomno)
        number_of_row_in_room = room.rows
        number_of_col_in_room = room.columns

        # Fetch student register numbers from the database
        register_data = Details.objects.values_list('RegNo', flat=True).distinct()
        if(len(register_data) > number_of_col_in_room*number_of_row_in_room):
            return 
        # Create a dictionary to group students by prefix
        students_by_prefix = {}
        for student in register_data:
            prefix = student[:8]
            if prefix not in students_by_prefix:
                students_by_prefix[prefix] = []
            students_by_prefix[prefix].append(student)

        # Create a list to store the final seating plan
        seatingPlan = []

        # Generate sequential orders for each prefix
        for prefix, students in students_by_prefix.items():
            sequential_order = [f'{prefix}{i:02}' for i in range(1, len(students) + 1)]
            students_by_prefix[prefix] = sequential_order

        # Arrange students ensuring no same-prefix students are adjacent
        while any(students_by_prefix.values()):
            for prefix in students_by_prefix.keys():
                if students_by_prefix[prefix]:
                    student = students_by_prefix[prefix].pop(0)
                    seatingPlan.append(student)

        x, y, z = 1, number_of_row_in_room, number_of_col_in_room

        # Fill any remaining seats with '0'
        seatingPlan += ['0' for _ in range(number_of_row_in_room * number_of_col_in_room - len(seatingPlan))]

        arr = np.array(seatingPlan, dtype=str).reshape((x, y, z))


        return render(request, 'seating_plan.html', {'roomno': roomno, 'seating_plan': arr})
    else:
        return render(request, 'room_selection.html')
'''