from storeadmin.models import Manufacture, Aircraftmodels, Service
from django.forms import ModelForm
from django import forms
import re


class ManufactureForm(ModelForm):
    class Meta:
        model = Manufacture
        fields = "__all__"
        widgets = {
            'Manufacture_name': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        print("inside clean")
        cleaned_date = super().clean()
        manufacture_name = cleaned_date.get('Manufacture_name')
        if manufacture_name is None:
            print("inside man")
            message = "Enter Manufacture Name"
            self.add_error('Manufacture_name', message)

        # x = '[a-zA-Z]'
        # matcher = re.fullmatch(x, manufacture_name)
        # if matcher is not None:
        #     print("inside matcher")
        # else:
        #     message = "Enter words only"
        #     self.add_error('Manufacture_name', message)


class AircraftForm(ModelForm):
    class Meta:
        model = Aircraftmodels
        fields = "__all__"
        widgets = {
            'Aircraft_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_model': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_seats': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_length': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_wingspan': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_fuel': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_ceiling': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_range': forms.TextInput(attrs={'class': 'form-control'}),
            # 'Aircraft_engine': forms.TextInput(attrs={'class': 'form-control'}),
            'Aircraft_price': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        print("Inside Aircraft Clean")
        cleaned_data = super().clean()
        aircraft_name = cleaned_data.get('Aircraft_name')
        aircraft_model = cleaned_data.get('Aircraft_model')
        aircraft_seats = int(cleaned_data.get('Aircraft_seats'))
        if aircraft_seats < 100:
            message = "Enter seats higher than 180"
            self.add_error('Aircraft_seats', message)


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            'Service_price': forms.TextInput(attrs={'class': 'form-control'}),
            'Service_type': forms.TextInput(attrs={'class': 'form-control'})
        }
