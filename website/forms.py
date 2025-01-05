from django import forms
from .models import record
#create add record forms
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name","class":"form-control"}), label="" )
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name","class":"form-control"}), label="" )
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email","class":"form-control"}), label="" )
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone Number","class":"form-control"}), label="" )
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address","class":"form-control"}), label="" )
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City","class":"form-control"}), label="" )
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip Code","class":"form-control"}), label="" )

    class Meta:
        model = record
        exclude = ("user",)