from django import forms
from django.conf import Settings
from django.forms import ModelForm
from .models import *
from django import forms


class FormularioRubro(ModelForm):
    class Meta:
        model = Rubro
        fields = ("nombre",)
        widgets = {"nombre": forms.TextInput(attrs={"class":"form-control"})}
        
        
class FormularioGasto(ModelForm):
    class Meta:
        model = Gasto
        fields = ("fecha","rubro","descripcion","importe")
        
        widgets = {"fecha": forms.TextInput(attrs={"class":"form-control"}),
                  "rubro": forms.Select(attrs={"class":"form-control"}),
                  "descripcion": forms.TextInput(attrs={"class":"form-control"}),
                  "importe": forms.TextInput(attrs={"class":"form-control"}),
                  }
        
