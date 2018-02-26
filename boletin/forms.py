from django import forms
from .models import Registrado
class RegForm(forms.Form):
	nombre=forms.CharField(max_length=100)
	email=forms.EmailField()

class ModelRegForm(forms.ModelForm):
	modelo=Registrado
	fields=["nombre","email"]
	class Meta:
		def clean_nombre(self):
			email=self.cleaned_data.get("nombre")
			return nombre
