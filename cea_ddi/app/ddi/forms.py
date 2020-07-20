from django import forms
from app.ddi.models import Expediente
from app.ddi.models import Desarrolladora
from app.ddi.models import Categorias
from app.ddi.models import SubCategorias
from app.ddi.models import Proyectos
from app.ddi.models import Aprobados

class ExpForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets ={
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'fraccionamiento': forms.TextInput(attrs={'class':'form-control'})
        }

class DesaForm(forms.ModelForm): 
    class Meta:
        model = Desarrolladora
        fields = '__all__'
        widgets ={
            'representante': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'})
        }

class CateForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SubCateForm(forms.ModelForm):
    class Meta:
        model = SubCategorias
        fields = '__all__'
        widgets = {
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProyeForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'

class AproForm(forms.ModelForm):
    class Meta:
        model = Aprobados
        fields = '__all__'

