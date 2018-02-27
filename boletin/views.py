from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
def inicio(request):
	form=RegForm()
	contexto={
		"mi_formulario":form,
	}
	return render(request,"inicio.html",contexto)
# Create your views here.
