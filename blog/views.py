from datetime import datetime
from django.shortcuts import get_object_or_404, render,redirect, get_list_or_404
from django.views.generic import View
from .models import *
from django.db.models import Count
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None
    return render(request, 'blog/login.html', {'error_message': error_message})



def Home(request):
    return render(request,'blog/base.html')


def check(request):
    contxt = {
    'username': request.user.username,
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,}
    return render(request,'blog/boilerplate.html',contxt)


@login_required(login_url='login')
def dashboard(request):
    org = get_object_or_404(Organization_Details, id=5)

    hardware_type_counts = Hardware.objects.values('hardware_type__name').annotate(total=Count('hardware_type'))
    software_type_counts = Software.objects.values('software_type__name').annotate(total=Count('software_type'))
    app_config = apps.get_app_config('blog')
    models = app_config.get_models()
    model_names = [model.__name__ for model in models]
    
       
    context ={
        'counts':hardware_type_counts,
        'models':model_names,
        'counts2':software_type_counts,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'org':org,
    }
    return render(request,'blog/dashboard.html',context)


def for_boiler(request):
    organization = Organization_Details.objects.get(pk=1)
    context = {
        'organization_name':organization.name,
    }
    return render(request,'blog/boilerplate.html',context)



def hardware_list(request):
    org = get_object_or_404(Organization_Details, id=5)

    hardware_types = HardwareType.objects.all()
    context = {
        'hardware_types': hardware_types,
        'org':org
    }
    return render(request, 'blog/hardwaretypedetails.html', context)

def add_hardware(request):
    org = get_object_or_404(Organization_Details, id=5)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        hardware_type = HardwareType(name=name, description=description)
        hardware_type.save()
        return redirect('hardware_list')
    else:
        return render(request, 'blog/hardwaretype.html',{'org':org})
    
@require_POST
def delete_hardware(request):
    hardware_ids = request.POST.getlist('hardware_ids')
    HardwareType.objects.filter(id__in=hardware_ids).delete()
    return redirect('hardware_list')

def edit_hardware(request, hardware_id):
    org = get_object_or_404(Organization_Details, id=5)
    hardware = get_object_or_404(HardwareType, id=hardware_id)
    if request.method == 'POST':
        hardware.name = request.POST.get('name')
        hardware.description = request.POST.get('description')
        hardware.save()
        return redirect('hardware_list')
    context = {
        'hardware': hardware,
        'org':org
    }
    return render(request, 'blog/edit_hardware.html',context)

from .forms import OrganizationDetailsForm,StatusDeleteForm, StatusRestoreForm

@login_required(login_url='login')
def edit_organization(request):
    org = get_object_or_404(Organization_Details, id=5)
    context = {
    'username': request.user.username,
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'org': org
    }
    if request.method == 'POST':
        # update the organization details using data from the POST request
        org.name = request.POST.get('name', org.name)
        org.code = request.POST.get('code', org.code)
        org.established_year = request.POST.get('established_year', org.established_year)
        org.country = request.POST.get('country', org.country)
        org.state = request.POST.get('state', org.state)
        org.city = request.POST.get('city', org.city)
        org.postal_code = request.POST.get('postal_code', org.postal_code)
        org.address = request.POST.get('address', org.address)
        org.phone = request.POST.get('phone', org.phone)
        org.fax = request.POST.get('fax', org.fax)
        org.email = request.POST.get('email', org.email)
        org.website = request.POST.get('website', org.website)
        org.logo = request.FILES.get('logo', org.logo)
        org.save()
    return render(request, 'blog/edit_organization.html',context)


def state_list(request):
    states = State.objects.filter(is_deleted=False)    
    context = {
        'states': states,
    }
    return render(request, 'blog/statedetails.html', context)


def add_state(request):
    org = get_object_or_404(Organization_Details, id=5)

    if request.method == 'POST':
        name = request.POST.get('name')
        state = State(name=name)
        state.save()
        return redirect('delete_state')
    else:
        return render(request, 'blog/addstate.html',{'org':org})
    
# def delete_state(request):
#     org = get_object_or_404(Organization_Details, id=5)
    
#     if request.method == 'POST':
#         selected_state_ids = request.POST.getlist('state_ids')
#         State.objects.filter(id__in=selected_state_ids).update(is_deleted=True)
#         return redirect('delete_state')
#     else:
#         states = State.objects.filter(is_deleted=False)
#     context = {
#         'states': states,
#         'org':org,
#         'first_name': request.user.first_name,
#         'last_name': request.user.last_name,
#     }
#     return render(request, 'blog/statedetails.html', context)

@require_POST
def delete_state(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).update(is_deleted=True)
    return redirect('trash_state')




def trash_state(request):
    trashed_states = State.objects.filter(is_deleted=True)
    context = {'trashed_states': trashed_states}
    return render(request, 'blog/trashstate.html', context)

@require_POST
def restore_state(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).update(is_deleted=False)
    return redirect('state')

# @require_POST
# def delete_state_permanently(request):
#     state_ids = request.POST.getlist('state_ids')
#     State.objects.filter(id__in=state_ids).delete()
#     return redirect('trash_state')

@require_POST
def delete_state_permanently(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).delete()
    return redirect('trash_state')
