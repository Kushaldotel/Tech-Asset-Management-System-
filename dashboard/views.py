from django import apps
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import *
from django.db.models import Count, Sum
from django.apps import apps

# Create your views here.
def new_dashboard(request):
    
    org = get_object_or_404(Organization_Details, id=5)
    asset = Asset.objects.get(id=1)
    
    hardware_type_counts = Hardware.objects.values('hardware_type__name').annotate(total=Count('hardware_type'))
    software_type_counts = Software.objects.values('software_type__name').annotate(total=Count('software_type'))
    document_type_counts = Document.objects.values('category__name').annotate(total=Count('category'))
    service_type_counts = Service.objects.values('service_type__name').annotate(total=Count('service_type'))
    app_config = apps.get_app_config('dashboard')
   
    models = app_config.get_models()
    model_names = [model.__name__ for model in models]
    count = Software.objects.count()
    count2 = Hardware.objects.count()
    service_count = Service.objects.count()
    document_count = Document.objects.count()
    user_count = User.objects.count()
    
    software_total = Software.objects.aggregate(total=Sum('purchase_price'))['total'] or 0
    service_total = Service.objects.aggregate(total=Sum('purchase_price'))['total'] or 0
    hardware_total = Hardware.objects.aggregate(total=Sum('purchase_price'))['total'] or 0
    overall_total = software_total + service_total + hardware_total

    pending_issue_count = Issue.objects.filter(status='Pending').count()
    
    hardware_area_chart = Hardware.objects.all()
    context ={
        'counts':hardware_type_counts,
        'models':model_names,
        'counts2':software_type_counts,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'org':org,
        'count_software':count,
        'count_hardware':count2,
        'service_count':service_count,
        'document_count':document_count,
        'user_count':user_count,
        'software_total': software_total, 'service_total': service_total, 'hardware_total': hardware_total, 'overall_total': overall_total,
        'document_type': document_type_counts,
        'service_type': service_type_counts,
        'hardware_area_chart': hardware_area_chart,
        'pending_issue_count': pending_issue_count,
    }
    if asset.dashboard_value==True:
        return render(request,'dashboard/dashboard.html',context)
    else:
        return redirect('software_list')
    # return JsonResponse({'error': 'Module Dashboard is disabled'})