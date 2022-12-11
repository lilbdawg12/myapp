from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def services(request):
    return render(request, 'hello/index1.html')





