from django import forms
from django.forms import fields

from . models import BLOOD_GROUP_CHOICES, Staffs
from akira_apps.academic_registration.models import BRANCH_CHOICES

class StaffsForm(forms.ModelForm):
    class Meta:
        model = Staffs
        blood_group = forms.ChoiceField(choices = BLOOD_GROUP_CHOICES)
        branch = forms.ChoiceField(choices = BRANCH_CHOICES)
        fields = ['gender','date_of_birth','door_no','zip_code','city_name','state_name','country_name','profile_pic','current_medical_issue','blood_group']