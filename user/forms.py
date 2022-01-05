from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Details

States = [    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttarakhand',
    'Uttar Pradesh',
    'West Bengal',
   'Andaman and Nicobar Islands',
    'Chandigarh',
    'Dadra and Nagar Haveli',
    'Daman & Diu',
    'The Government of NCT of Delhi',
    'Jammu & Kashmir',
    'Ladakh',
    'Lakshadweep',
    'Puducherry',
]

def create_dict():
    return ((i,i) for i in States)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']


class DetailsForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10, min_length=10, widget = forms.TextInput(attrs = {'pattern': '[0-9]{10}'}))
    state = forms.ChoiceField(choices=create_dict())
    city = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    postcode = forms.CharField(max_length=6, min_length=6, widget = forms.TextInput(attrs = {'pattern': '[0-9_]{6}'}))

    class Meta:
        model = Details
        fields = ['name', 'phone', 'state', 'city',  'address', 'postcode']

