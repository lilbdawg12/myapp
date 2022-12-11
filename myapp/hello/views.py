from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def services(request):
    return render(request, 'hello/index1.html')

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')

def feedback(request):
    return render(request, 'hello/feedback.html')





