from django import forms
from .models import *

class OrganizationDetailsForm(forms.ModelForm):
    class Meta:
        model = Organization_Details
        fields = ['name', 'code', 'established_year', 'country', 'state', 'city', 'postal_code', 'address', 'phone', 'fax', 'email', 'website', 'logo', 'branches']
        widgets = {
            'branches': forms.CheckboxSelectMultiple
        }


class StatusDeleteForm(forms.Form):
    status_ids = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), widget=forms.CheckboxSelectMultiple)

class StatusRestoreForm(forms.Form):
    status_ids = forms.ModelMultipleChoiceField(queryset=Status.objects.none(), widget=forms.CheckboxSelectMultiple)

# class IssueForm(forms.ModelForm):
#     class Meta:
#         model = Issue
#         fields = ['asset_category', 'title', 'assigned_to', 'category', 'asset_name','status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     asset_category = self.initial.get('asset_category')
    #     # status = self.initial.get('status')
    #     if asset_category == 'Hardware':
    #         self.fields['asset_name'].queryset = Hardware.objects.all()
    #     elif asset_category == 'Software':
    #         self.fields['asset_name'].queryset = Software.objects.all()
    #     elif asset_category == 'Document':
    #         self.fields['asset_name'].queryset = Document.objects.all()
    #     elif asset_category == 'Service':
    #         self.fields['asset_name'].queryset = Service.objects.all()
            
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, HTML, Field


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['asset_category', 'title', 'assigned_to', 'category', 'asset_name', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3 control-label'
        self.helper.field_class = 'col-sm-8'
        self.helper.layout = Layout(
            Fieldset(
                'Issue Details',
                Div('asset_category', css_class='form-group'),
                Div('title', css_class='form-group'),
                Div('assigned_to', css_class='form-group'),
                Div('category', css_class='form-group'),
                Div('asset_name', css_class='form-group'),
                Div('status', css_class='form-group'),
                css_class='col-sm-12',
                css_id='issue-details'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
            ),
        )
  
class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['asset_category', 'title', 'assigned_to', 'category', 'asset_name', 'status']
    

class AssetRequestForm(forms.ModelForm):
    class Meta:
        model = AssetRequest
        fields = ('asset_type', 'asset_name', 'tentative_cost', 'branch', 'department', 'description', 'priority', 'status')
        
        
class SoftwareTypeForm(forms.ModelForm):
    class Meta:
        model = SoftwareType
        fields = ['name', 'description', 'vendor']
class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = Service_Category
        fields = ['name', 'vendor']
class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentCategory
        fields = ['name', 'description']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
         
class ManagedByForm(forms.ModelForm):
    class Meta:
        model = ManagedBy
        fields = '__all__'
        
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        
class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'
        
class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = '__all__'
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'