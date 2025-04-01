from django.shortcuts import render


from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    
    return render(request, 'upload.html', {'form': form})

def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})

