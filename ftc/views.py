from django.shortcuts import render
from django.http import FileResponse, Http404
from django.templatetags.static import static
# Create your views here.
def home(request):
    # try:
    url="ftc/"+static('Readme.pdf')
    
    return FileResponse(open(url,'rb'),content_type="application/pdf")
    # except FileNotFoundError:
        
    #     raise Http404()

