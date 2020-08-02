from django import forms
from app.ddi.models import Expediente
from app.ddi.models import Desarrolladora
from app.ddi.models import Categorias
from app.ddi.models import SubCategorias
from app.ddi.models import Proyectos
from app.ddi.models import Aprobados
from app.ddi.models import Ingresos
from django.contrib.auth.models import User


class ExpForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'fraccionamiento': forms.TextInput(attrs={'class': 'form-control'})
        }


class DesaForm(forms.ModelForm):
    class Meta:
        model = Desarrolladora
        fields = '__all__'
        widgets = {
            'representante': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'propietario': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'})
        }


class CateForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SubCateForm(forms.ModelForm):
    class Meta:
        model = SubCategorias
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProyeForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = {'nombre', 'expediente', 'desarrolladora', 'tipo',
                  'responsable', 'revisador'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'expediente': forms.Select(attrs={'class': 'form-control'}),
            'desarrolladora': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'revisador': forms.Select(attrs={'class': 'form-control'}),
        }


class RevisarForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = {'oficio', 'fecha_respuesta', 'observaciones', 'status'}
        widgets = {
            'oficio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_respuesta': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingresos
        fields = {'folio', 'fecha_ingreso'}
        widgets = {
            'folio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'is_superuser'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }


class AproForm(forms.ModelForm):
    class Meta:
        model = Aprobados
        fields = '__all__'


class NotaForm(forms.Form):
    expediente = forms.ModelMultipleChoiceField(
        queryset=Expediente.objects, widget=forms.Select(attrs={'class': 'form-control'}))
    categoria = forms.ModelMultipleChoiceField(
        queryset=SubCategorias.objects, widget=forms.Select(attrs={'class': 'form-control'}))
    inicio = forms.DateTimeField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))
    fin = forms.DateTimeField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}))
