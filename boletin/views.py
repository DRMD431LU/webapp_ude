from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
def inicio(request):
	form=RegForm(request.POST or NONE)
	if form.is_valid():
		form_data=form.cleaned_data
		abc=form_data.get("email")
		abc2=form_data.get("email")
		obj=Registrado.objects.create(email=abc,nombre=abc2)
	contexto={
		"mi_formulario":form,
	}
	return render(request,"inicio.html",contexto)
# Create your views here.
