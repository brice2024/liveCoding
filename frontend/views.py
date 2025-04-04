from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm


#vue pour l'upload de fichiers
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    
    return render(request, 'upload.html', {'form': form})


#vue pour l'affichage de la liste des fichiers
def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})

