from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CSVUploadForm
from .models import Details
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

# Create your views here.
