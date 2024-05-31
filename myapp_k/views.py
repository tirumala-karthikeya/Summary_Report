import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']

            data = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
           
            summary = data.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')
            return render(request, 'myapp_k/summary.html', {'summary': summary.to_html(index=False)})
    else:
        form = UploadFileForm()
    return render(request, 'myapp_k/upload.html', {'form': form})
