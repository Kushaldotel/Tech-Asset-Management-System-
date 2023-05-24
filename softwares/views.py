from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def new_soft(request):
    # org = get_object_or_404(Organization_Details, id=5)
    software_list = Software.objects.all()
    
    if request.method == 'POST':
        selected_software = request.POST.getlist('selected_software')
        Software.objects.filter(id__in=selected_software).delete()
        return redirect('new_soft')
    
    context = {'software_list': software_list,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'softwares/software_list.html', context)