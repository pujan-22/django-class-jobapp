from django.shortcuts import render

from uploadapp.forms import UploadForm, UploadFileForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved = form.instance
            return render(request, 'uploadapp/add_image.html', {'form':form, 'saved':saved})
    else:
        form = UploadForm()
    return render(request, 'uploadapp/add_image.html', {'form':form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            saved = form.instance
            return render(request, 'uploadapp/add_file.html', {'form':form, 'saved':saved})
    else:
        form = UploadFileForm()
    return render(request, 'uploadapp/add_file.html', {'form':form})