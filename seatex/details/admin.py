from django.contrib import admin
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path
from .models import Details,RoomDetails
from .forms import CSVUploadForm
import csv
import io

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


