from turtle import width
from django import forms
from django.conf import Settings
from django.forms import ModelForm
from .models import *
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


class FormularioRubro(ModelForm):
    class Meta:
        model = Rubro
        fields = ("nombre",)
        widgets = {"nombre": forms.TextInput(attrs={"class":"form-control"})}
        
        
class FormularioGasto(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ("fecha","rubro","descripcion","importe")
        
        widgets = {"fecha": DatePickerInput(format='%d/%m/%y',attrs={"class":"form-control"}),
                  "rubro": forms.Select(attrs={"class":"form-control"}),
                  "descripcion": forms.TextInput(attrs={"class":"form-control"}),
                  "importe": forms.TextInput(attrs={"class":"form-control"}),
                  }
        
