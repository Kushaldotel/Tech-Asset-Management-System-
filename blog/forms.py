from django import forms
from .models import Organization_Details

class OrganizationDetailsForm(forms.ModelForm):
    class Meta:
        model = Organization_Details
        fields = ['name', 'code', 'established_year', 'country', 'state', 'city', 'postal_code', 'address', 'phone', 'fax', 'email', 'website', 'logo', 'branches']
        widgets = {
            'branches': forms.CheckboxSelectMultiple
        }


from django import forms
from .models import Status

class StatusDeleteForm(forms.Form):
    status_ids = forms.ModelMultipleChoiceField(queryset=Status.objects.all(), widget=forms.CheckboxSelectMultiple)

class StatusRestoreForm(forms.Form):
    status_ids = forms.ModelMultipleChoiceField(queryset=Status.objects.none(), widget=forms.CheckboxSelectMultiple)
