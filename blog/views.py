from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect, get_list_or_404
from django.views import View
from .models import *
from django.db.models import Count
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.db.models import Sum
from .forms import *





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

@login_required(login_url='login')
def check(request):
    org = get_object_or_404(Organization_Details, id=5)
    dashboard = True  # Set this value based on your condition
    enable_dashboard = True if dashboard else False
    context = {
    'username': request.user.username,
    'first_name': request.user.first_name,
    'last_name': request.user.last_name,
    'org':org,
    'enable_dashboard':enable_dashboard,}
    
    return render(request,'blog/boilerplate.html',context)


@login_required(login_url='login')
def dashboard(request):
    
    org = get_object_or_404(Organization_Details, id=5)
    asset = Asset.objects.get(id=1)
    
    hardware_type_counts = Hardware.objects.values('hardware_type__name').annotate(total=Count('hardware_type'))
    software_type_counts = Software.objects.values('software_type__name').annotate(total=Count('software_type'))
    document_type_counts = Document.objects.values('category__name').annotate(total=Count('category'))
    service_type_counts = Service.objects.values('service_type__name').annotate(total=Count('service_type'))
    app_config = apps.get_app_config('blog')
    
        
   
    models = app_config.get_models()
    model_names = [model.__name__ for model in models]
    count = Software.objects.count()
    count2 = Hardware.objects.count()
    service_count = Service.objects.count()
    document_count = Document.objects.count()
    user_count = User.objects.count()
    
    if asset.software_value==True:
        software_total = Software.objects.aggregate(total=Sum('purchase_price'))['total'] or 0
    else:
        software_total = 0
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
        return render(request,'blog/dashboard.html',context)
    return redirect('software_list')
    # return JsonResponse({'error': 'Module Dashboard is disabled'})


# def for_boiler(request):
#     organization = Organization_Details.objects.get(pk=1)
#     context = {
#         'organization_name':organization.name,
#     }
#     return render(request,'blog/boilerplate.html',context)



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

# def edit_hardware(request, hardware_id):
#     org = get_object_or_404(Organization_Details, id=5)
#     hardware = get_object_or_404(HardwareType, id=hardware_id)
#     if request.method == 'POST':
#         hardware.name = request.POST.get('name')
#         hardware.description = request.POST.get('description')
#         hardware.save()
#         return redirect('hardware_list')
#     context = {
#         'hardware': hardware,
#         'org':org
#     }
#     return render(request, 'blog/edit_hardware.html',context)

# from .forms import OrganizationDetailsForm,StatusDeleteForm, StatusRestoreForm

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

@login_required(login_url='login')

def state_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    states = State.objects.filter(is_deleted=False)    
    context = {
        'states': states,
        'org':org,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return render(request, 'blog/statedetails.html', context)

@login_required(login_url='login')

def add_state(request):
    
    org = get_object_or_404(Organization_Details, id=5)

    if request.method == 'POST':
        name = request.POST.get('name')
        state = State(name=name)
        state.save()
        return redirect('state')
    else:
        return render(request, 'blog/addstate.html',{'org':org})
    

@require_POST
def delete_state(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).update(is_deleted=True)
    return redirect('trash_state')

@require_POST
def delete_software(request):
    selected_software = request.POST.getlist('selected_software')
    Software.objects.filter(id__in=selected_software).update(is_deleted=True)
    return redirect('software_list')



@login_required(login_url='login')
def trash_state(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    trashed_states = State.objects.filter(is_deleted=True)
    context = {'trashed_states': trashed_states,
               'org':org}
    return render(request, 'blog/trashstate.html', context)


def trash_software(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    trashed_softwares = Software.objects.filter(is_deleted=True)
    context = {'trashed_softwares': trashed_softwares,
               'org':org}
    return render(request, 'blog/trashsoftware.html', context)


@require_POST
def restore_state(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).update(is_deleted=False)
    return redirect('state')


@require_POST
def restore_software(request):
    selected_software = request.POST.getlist('selected_software')
    Software.objects.filter(id__in=selected_software).update(is_deleted=False)
    return redirect('software_list')


@require_POST
def delete_state_permanently(request):
    state_ids = request.POST.getlist('state_ids')
    State.objects.filter(id__in=state_ids).delete()
    return redirect('trash_state')


@login_required(login_url='login')
def create_issue(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('issue')
    else:
        form = IssueForm()
    return render(request, 'blog/issue.html', {'form': form,'org':org})


@login_required(login_url='login')

def issue_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    issues = Issue.objects.all()

    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('delete')
        Issue.objects.filter(id__in=ids_to_delete).delete()
        return redirect('issue_list')
    context = {
        'org':org,
        'issues':issues,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return render(request, 'blog/issue_list.html', context)



@login_required(login_url='login')

def issue_detail(request, pk):
    org = get_object_or_404(Organization_Details, id=5)
    
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
    else:
        form = IssueForm(instance=issue)


    return render(request, 'blog/edit_issue.html', {'form': form,'org':org})


@login_required(login_url='login')
def create_issue_category(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        issue_category = Issue_Category(name=name, description=description)
        issue_category.save()
        return redirect('issue_category')

    return render(request, 'blog/create_issue_category.html',{'org':org})

@login_required(login_url='login')
def issue_Category_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    category = Issue_Category.objects.all()

    if request.method == 'POST':
        ids_to_delete = request.POST.getlist('delete')
        Issue_Category.objects.filter(id__in=ids_to_delete).delete()
        return redirect('issue_category')

    return render(request, 'blog/issue_category.html', {'categories': category,'org':org})

def issue_category_edit(request, pk):
    org = get_object_or_404(Organization_Details, id=5)
    
    category = get_object_or_404(Issue_Category, pk=pk)
    if request.method == 'POST':
        form = Issue_CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('issue_category')
    else:
        form = Issue_CategoryForm(instance=category)
    return render(request, 'blog/edit_issue_category.html', {'form': form,'org':org})



@login_required(login_url='login')
def asset_request_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    asset_requests = AssetRequest.objects.all()
    
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        AssetRequest.objects.filter(id__in=selected_ids).delete()
        return redirect('asset_request_list')
    
    context = {
        'asset_requests': asset_requests,
        'org':org
    }
    return render(request, 'blog/asset_request.html', context)


@login_required(login_url='login')
def add_asset_request(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    if request.method == 'POST':
        form = AssetRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_request_list')
    else:
        form = AssetRequestForm()
    
    context = {
        'form': form,
        'org':org
    }
    return render(request, 'blog/add_asset_request.html', context)

@login_required(login_url='login')
def asset_request_edit(request, pk):
    org = get_object_or_404(Organization_Details, id=5)
    
    asset = get_object_or_404(AssetRequest, pk=pk)
    if request.method == 'POST':
        form = AssetRequestForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_request_list')
    else:
        form = AssetRequestForm(instance=asset)
    return render(request, 'blog/edit_asset_request.html', {'form': form,'org':org})



@login_required(login_url='login')
def software_type_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    software_type = SoftwareType.objects.all()
    
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        SoftwareType.objects.filter(id__in=selected_ids).delete()
        return redirect('software_types')
    
    context = {
        'software_types': software_type,
        'org':org
    }
    return render(request, 'blog/softwaretype.html', context)



@login_required(login_url='login')
def create_software_type(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    vendors = Vendor.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        vendor_id = request.POST.get('vendor')
        vendor = Vendor.objects.get(id=vendor_id)
        
        software_type = SoftwareType(name=name, description=description, vendor=vendor)
        software_type.save()
        
        return redirect('software_types')  # Replace 'software_types_list' with the appropriate URL name for listing software types
    else:
        vendors = Vendor.objects.all()
    
    return render(request, 'blog/create_software_type.html', {'vendors': vendors,'org':org})


@login_required(login_url='login')
def edit_software_type(request, software_type_id):
    org = get_object_or_404(Organization_Details, id=5)
    
    software_type = get_object_or_404(SoftwareType, id=software_type_id)
    
    if request.method == 'POST':
        form = SoftwareTypeForm(request.POST, instance=software_type)
        if form.is_valid():
            form.save()
            return redirect('software_types')  # Replace 'software_types_list' with the appropriate URL name for listing software types
    else:
        form = SoftwareTypeForm(instance=software_type)
    
    return render(request, 'blog/edit_software_type.html', {'form': form,'org':org})




@login_required(login_url='login')
def service_type_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    service_type = Service_Category.objects.all()
    
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        Service_Category.objects.filter(id__in=selected_ids).delete()
        return redirect('software_types')
    
    context = {
        'service_types': service_type,
        'org':org
    }
    return render(request, 'blog/service_type.html', context)


@login_required(login_url='login')
def create_service_type(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    service_type = Service_Category.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        vendor_id = request.POST.get('vendor')
        vendor = Vendor.objects.get(id=vendor_id)
        
        service_type = Service_Category(name=name,vendor=vendor)
        service_type.save()
        
        return redirect('service_types')  
    else:
        vendors = Vendor.objects.all()
    
    return render(request, 'blog/create_service_type.html', {'vendors': vendors,'org':org})



@login_required(login_url='login')
def edit_service_type(request, service_type_id):
    org = get_object_or_404(Organization_Details, id=5)
    
    service_type = get_object_or_404(Service_Category, id=service_type_id)
    
    if request.method == 'POST':
        form = ServiceTypeForm(request.POST, instance=service_type)
        if form.is_valid():
            form.save()
            return redirect('service_types')
    else:
        form = ServiceTypeForm(instance=service_type)
    
    return render(request, 'blog/edit_software_type.html', {'form': form,'org':org})



def document_type_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    document_types = DocumentCategory.objects.all()
    
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        DocumentCategory.objects.filter(id__in=selected_ids).delete()
        # messages.success(request, 'Selected document types have been deleted.')
        return redirect('document_types')
    
    context = {
        'document_types': document_types,
        'org': org,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return render(request, 'blog/document_type.html', context)



@login_required(login_url='login')
def create_document_type(request):
    org = get_object_or_404(Organization_Details, id=5)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        software_type = DocumentCategory(name=name, description=description)
        software_type.save()
        
        return redirect('document_types')        
    
    return render(request, 'blog/create_document_type.html', {'org':org})


@login_required(login_url='login')
def edit_document_type(request, document_type_id):
    org = get_object_or_404(Organization_Details, id=5)
    
    document_type = get_object_or_404(DocumentCategory, id=document_type_id)
    
    if request.method == 'POST':
        form = DocumentTypeForm(request.POST, instance=document_type)
        if form.is_valid():
            form.save()
            return redirect('document_types')
    else:
        form = DocumentTypeForm(instance=document_type)
    
    return render(request, 'blog/edit_document_type.html', {'form': form,'org':org})



class BranchListView(View):
    
    def get(self, request):
        org = get_object_or_404(Organization_Details, id=5)
        branches = Branch.objects.all()
        return render(request, 'blog/branch_list.html', {'branches': branches,'org':org,
                                                         'first_name': request.user.first_name,
                                                         'last_name': request.user.last_name,})

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')
        Branch.objects.filter(id__in=selected_items).delete()
        return redirect('branch_list')

class VendorListView(View):
    def get(self, request):
        org = get_object_or_404(Organization_Details, id=5)
        
        vendors = Vendor.objects.all()
        return render(request, 'blog/vendor_list.html', {'vendors': vendors,'org':org})

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')
        Vendor.objects.filter(id__in=selected_items).delete()
        return redirect('vendor_list')

class AddBranchView(View):

    def get(self, request):
        org = get_object_or_404(Organization_Details, id=5)

        form = BranchForm()
        return render(request, 'blog/add_branch.html', {'form': form,
                'org': org,                                                      
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})

    def post(self, request):
        form = BranchForm(request.POST)
        org = get_object_or_404(Organization_Details, id=5)
        
        if form.is_valid():
            form.save()
            return redirect('branch_list')
        return render(request, 'blog/add_branch.html', {'form': form,
                                                                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})
class AddVendorView(View):
    

    def get(self, request):
        org = get_object_or_404(Organization_Details, id=5)
        form = VendorForm()
        return render(request, 'blog/add_vendor.html', {'form': form,
                                                                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})

    def post(self, request):
        form = VendorForm(request.POST)
        org = get_object_or_404(Organization_Details, id=5)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
        return render(request, 'blog/add_vendor.html', {'form': form,               'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})
    
class EditBranchView(View):

    def get(self, request, branch_id):
        org = get_object_or_404(Organization_Details, id=5)
        branch = get_object_or_404(Branch, id=branch_id)
        form = BranchForm(instance=branch)
        return render(request, 'blog/edit_branch.html', {'form': form, 'branch': branch,
                                                         'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})

    def post(self, request, branch_id):
        org = get_object_or_404(Organization_Details, id=5)
        branch = get_object_or_404(Branch, id=branch_id)
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_list')
        return render(request, 'blog/edit_branch.html', {'form': form, 'branch': branch,
                                                                        'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})
class EditVendorView(View):
    

    def get(self, request, vendor_id):
        org = get_object_or_404(Organization_Details, id=5)
        vendor = get_object_or_404(Vendor, id=vendor_id)
        form = VendorForm(instance=vendor)
        return render(request, 'blog/edit_vendor.html', {'form': form, 'vendor': vendor,
                                                        'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name, })

    def post(self, request, vendor_id):
        org = get_object_or_404(Organization_Details, id=5)
        vendor = get_object_or_404(Vendor, id=vendor_id)
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
        return render(request, 'blog/edit_vendor.html', {
            'form': form, 'vendor': vendor,
                 'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,})
    

def department_list(request):
    departments = ManagedBy.objects.all()
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        selected_departments = request.POST.getlist('selected_departments')
        ManagedBy.objects.filter(id__in=selected_departments).delete()
        return redirect('department_list')
    
    context = {
        'departments': departments,
                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
    }
    return render(request, 'blog/department_list.html', context)

def add_department(request):
    form = ManagedByForm()
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        form = ManagedByForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')

    context = {
        'form': form,
                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
    }
    return render(request, 'blog/add_department.html', context)

def edit_department(request, department_id):
    department = get_object_or_404(ManagedBy, id=department_id)
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        form = ManagedByForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = ManagedByForm(instance=department)

    context = {
        'form': form,
        'department': department,
                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
    }
    return render(request, 'blog/edit_department.html', context)


def hardware_list(request):
    hardware_list = Hardware.objects.all()
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        selected_hardware = request.POST.getlist('selected_hardware')
        Hardware.objects.filter(id__in=selected_hardware).delete()
        return redirect('hardware_list')

    context = {'hardware_list': hardware_list,
                              'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/hardware_list.html', context)

def add_hardware(request):
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hardware_list')
    else:
        form = HardwareForm()

    context = {'form': form,
                              'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/add_hardware.html', context)

def edit_hardware(request, hardware_id):
    org = get_object_or_404(Organization_Details, id=5)
    hardware = get_object_or_404(Hardware, id=hardware_id)

    if request.method == 'POST':
        form = HardwareForm(request.POST, instance=hardware)
        if form.is_valid():
            form.save()
            return redirect('hardware_list')
    else:
        form = HardwareForm(instance=hardware)

    context = {
        'form': form,
        'hardware': hardware,
                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
    }
    return render(request, 'blog/edit_hardware.html', context)


# @login_required(login_url='login')
def software_list(request):
    org = get_object_or_404(Organization_Details, id=5)
    # software_list = Software.objects.all()
    software_list = Software.objects.filter(is_deleted=False)    
    
    asset = Asset.objects.get(id=1)
    
    if asset.software_value==False:
        return JsonResponse({'software_Module': 'Disabled'})
    
    
    if request.method == 'POST':
        selected_software = request.POST.getlist('selected_software')
        Software.objects.filter(id__in=selected_software).delete()
        return redirect('software_list')
    
    context = {'software_list': software_list,
                'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/software_list.html', context)

def add_software(request):
    org = get_object_or_404(Organization_Details, id=5)
    asset = Asset.objects.get(id=1)
    
    if asset.software_value==False:
        return JsonResponse({'software_Module': 'Disabled'})
    
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = SoftwareForm()

    context = {'form': form,
                              'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/add_software.html', context)

def edit_software(request, software_id):
    software = get_object_or_404(Software, id=software_id)
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = SoftwareForm(instance=software)

    context = {'form': form, 'software': software,
                              'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/edit_software.html', context)


def document_list(request):
    document_list = Document.objects.all()
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        selected_documents = request.POST.getlist('selected_documents')
        Document.objects.filter(id__in=selected_documents).delete()
        return redirect('document_list')

    context = {'document_list': document_list,
                              'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/document_list.html', context)

def add_document(request):
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'blog/add_document.html', {'form': form,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
               'org': org,})

def edit_document(request, document_id):
    org = get_object_or_404(Organization_Details, id=5)
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm(instance=document)

    context = {
        'form': form,
        'document': document,
                       'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
    }
    return render(request, 'blog/edit_document.html', context)


@login_required(login_url='login')
def service_list(request):
    service_list = Service.objects.all()
    org = get_object_or_404(Organization_Details, id=5)
    
    if request.method == 'POST':
        selected_services = request.POST.getlist('selected_services')
        Service.objects.filter(id__in=selected_services).delete()
        return redirect('service_list')

    context = {'service_list': service_list,
               'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,}
    return render(request, 'blog/service_list.html', context)



def add_service(request):
    org = get_object_or_404(Organization_Details, id=5)
    if request.method == 'POST':
        # Extract form data
        name = request.POST['name']
        service_type_id = request.POST['service_type']
        criticality_id = request.POST['criticality']
        managed_by_id = request.POST['managed_by']
        document_id = request.POST['document']
        purchase_price = request.POST['purchase_price']
        purchase_date = request.POST['purchase_date']
        expiry_date = request.POST['expiry_date']
        status_id = request.POST['status']

        # Create a new Service object
        service = Service(
            name=name,
            service_type_id=service_type_id,
            criticality_id=criticality_id,
            managed_by_id=managed_by_id,
            document_id=document_id,
            purchase_price=purchase_price,
            purchase_date=purchase_date,
            expiry_date=expiry_date,
            status_id=status_id
        )

        # Save the service object
        service.save()

        # Redirect to a success page or any other desired page
        return redirect('service_list')

    else:
        # Get the data for foreign key fields
        service_categories = Service_Category.objects.all()
        criticalities = Criticality.objects.all()
        managers = ManagedBy.objects.all()
        documents = Document.objects.all()
        statuses = Status.objects.all()

        context = {
            'service_categories': service_categories,
            'criticalities': criticalities,
            'managers': managers,
            'documents': documents,
            'statuses': statuses,
            'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
        }

        return render(request, 'blog/add_service.html', context)
    

def edit_service(request, service_id):
    service = Service.objects.get(id=service_id)
    form = ServiceForm(instance=service)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')

    context = {
        'form': form,
        'service': service,
    }
    return render(request, 'blog/edit_service.html', context)

from django.contrib.auth.decorators import user_passes_test
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def button_handler(request):
    org = get_object_or_404(Organization_Details, id=5)
    assets = Asset.objects.all()
    context = {

            'org': org,
               'first_name': request.user.first_name,
               'last_name': request.user.last_name,
               'assets': assets,
    }
    return render(request, 'blog/button_handler.html',context)


def toggle_hardware_value(request):
    if request.method == 'POST':
        asset_id = request.POST.get('asset_id')
        asset = get_object_or_404(Asset, id=asset_id)

        asset.dashboard_value = not asset.dashboard_value  # Toggle the value
        asset.save()

    return redirect('buttons')

def toggle_software_value(request):
    if request.method == 'POST':
        asset_id = request.POST.get('value_id')
        asset = get_object_or_404(Asset, id=asset_id)

        asset.software_value = not asset.software_value  # Toggle the value
        asset.save()

    return redirect('buttons')



def sss(request):
    # criticalities = Criticality.objects.all()
    # context = {
    #     'criticalities': criticalities,
    # }
    hardware_types = HardwareType.objects.all()
    vendors = Vendor.objects.all()
    criticalities = Criticality.objects.all()
    branches = Branch.objects.all()
    managed_bys = ManagedBy.objects.all()
    documents = Document.objects.all()
    statuses = Status.objects.all()
    insurances = Insurance.objects.all()

    context = {
        'hardware_types': hardware_types,
        'vendors': vendors,
        'criticalities': criticalities,
        'branches': branches,
        'managed_bys': managed_bys,
        'documents': documents,
        'statuses': statuses,
        'insurances': insurances,
    }

    
    return render(request, 'blog/ssss.html',context)