from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request,'index.html',{})

def primertemplate (request):
    return render (request, 'primertemplate.html', {})