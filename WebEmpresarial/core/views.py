from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')
def about(request):
    return render(request,'core/about.html')

def sample(request):
    return render(request ,'core/sample.html')

def store(request):
    return render(request,'core/store.html')