from django.contrib import admin
from django.http import HttpResponseRedirect,HttpResponse
from django.template.response import TemplateResponse
from django.urls import path
from .models import Details,RoomDetails
from .forms import CSVUploadForm
import csv
import io
def generate_seating_arrangement(modeladmin, request, queryset):
    # Create a dictionary to store room information
    rooms = {}
    for room_info in RoomDetails.objects.all():
        rooms[room_info.roomno] = {
            'rows': room_info.rows,
            'columns': room_info.columns,
            'benches': room_info.noofbenches,
            'bench_strength': room_info.benchstrength,
            'students': []
        }

    # Create a list of students
    students = [student.RegNo for student in queryset]

    # Calculate the total number of students to be assigned
    total_students = len(students)

    # Initialize variables to keep track of current student and room
    current_student = 0

    # Assign students to rooms sequentially
    for room_number, room_info in rooms.items():
        for i in range(room_info['rows']):
            for j in range(room_info['columns']):
                if current_student < total_students:
                    room_info['students'].append(students[current_student])
                    current_student += 1

    # Create a CSV response for the seating arrangement
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="seating_arrangement.csv"'

    csv_writer = csv.writer(response)
    for room_number, room_info in rooms.items():
        for i in range(room_info['rows']):
            row_data = []
            for j in range(room_info['columns']):
                student_index = i * room_info['columns'] + j
                if student_index < len(room_info['students']):
                    row_data.append(room_info['students'][student_index])
                else:
                    row_data.append("Empty")
            csv_writer.writerow(row_data)

    return response

generate_seating_arrangement.short_description = "Download Seating Arrangement CSV"
@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_csv_upload.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                self.handle_csv_file(request.FILES['csv_file'])
                self.message_user(request, "CSV file uploaded successfully.")
                return HttpResponseRedirect("..")
        else:
            form = CSVUploadForm()

        payload = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Upload CSV',
        }
        return TemplateResponse(request, "admin/upload_csv.html", payload)

    def handle_csv_file(self, csv_file):
        csv_data = csv_file.read().decode('utf-8')
        reader = csv.reader(io.StringIO(csv_data))

        for row in reader:
            status = row[0]  # Assuming the status is in the first column
            reg_no = row[1]  # Assuming the RegNo is in the second column

            details = Details(status=status, RegNo=reg_no)
            details.save()

    list_display = ('status', 'RegNo')
    actions = [generate_seating_arrangement]

@admin.register(RoomDetails)
class RoomDetailsAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_rcsv_upload.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return custom_urls + urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                self.handle_csv_file(request.FILES['csv_file'])
                self.message_user(request, "CSV file uploaded successfully.")
                return HttpResponseRedirect("..")
        else:
            form = CSVUploadForm()

        payload = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Upload CSV',
        }
        return TemplateResponse(request, "admin/upload_room_details_csv.html", payload)

    def handle_csv_file(self, csv_file):
        csv_data = csv_file.read().decode('utf-8')
        reader = csv.reader(io.StringIO(csv_data))

        for row in reader:
            roomno = row[0]  # Assuming the roomno is in the first column
            rows = row[1]  # Assuming the rows is in the second column
            columns = row[2]  # Assuming the columns is in the third column
            noofbenches = row[3]  # Assuming the noofbenches is in the fourth column
            benchstrength = row[4]  # Assuming the benchstrength is in the fifth column

            room_details = RoomDetails(roomno=roomno, rows=rows, columns=columns, noofbenches=noofbenches, benchstrength=benchstrength)
            room_details.save()
        list_display = ('roomno', 'rows', 'columns', 'noofbenches', 'benchstrength')
