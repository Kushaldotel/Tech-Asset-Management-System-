from django.shortcuts import render
# Create your views here.
def Index(request):
    return render(request,'blog/home.html')
def check(request):
    return render(request,'blog/test.html')