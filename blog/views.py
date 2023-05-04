from django.shortcuts import render
# Create your views here.
def Index(request):
    # return render(request,'blog/home.html')
    pass
def check(request):
    return render(request,'blog/test.html')

def Admin(request):
    return render(request,'blog/home.html')