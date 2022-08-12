from contextvars import Context
import os
from urllib import response
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse
from app.models import Upload

# Create your views here.

def index(request): 
    context = {'file':Upload.objects.all()}
    return render(request, 'index.html', context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/song")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    
    raise Http404

def search(request):
    title = 'Serach Page'
    try:
        if request.method == 'GET':
            title = request.GET.get('title')
            count = Upload.objects.filter(title__icontains=title).count()
            context = {'file':Upload.objects.filter(title__icontains=title), 'count':count}
            print("Thid is count right here",count)
    except Exception as e:
        print(e)
        return HttpResponse('<h1>Error!!! please input correct search options</h1>')
    return render(request, 'index.html', context)