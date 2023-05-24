import os
import zipfile
from django.conf import settings
from django.shortcuts import render
from .forms import UploadZipForm
from .models import UploadedApp

def upload_zip(request):
    if request.method == 'POST':
        form = UploadZipForm(request.POST, request.FILES)
        if form.is_valid():
            zip_file = request.FILES['zip_file']
            uploaded_app = UploadedApp(zip_file=zip_file)
            uploaded_app.save()

            # Extracting the zip file
            extract_path = 'C:\Developer\Django\mysql\djangomysql'
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            # Custom code to handle the extracted files, e.g., moving them to the desired location, registering the new app, etc.

            return render(request, 'upload_success.html')
    else:
        form = UploadZipForm()
    
    return render(request, 'upload.html', {'form': form})
