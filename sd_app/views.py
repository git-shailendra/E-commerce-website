from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def s(request):
    return render(request, 'SD/index.html')

def d(request):
    return render(request, 'SD/second.html')

def k(request):
    return render(request, 'SD/third.html')

def v(request):
    return render(request, 'SD/fourth.html')

def m(request):
    return render(request, 'SD/fifth.html')

