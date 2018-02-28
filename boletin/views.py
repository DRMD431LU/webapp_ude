from django.shortcuts import render
from .forms import RegForm,RegModelForm
from .models import Registrado
def inicio(request):
	titulo="hola"
	if request.user.is_authenticated():
		titulo="bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		print (instance)
		# form_data=form.cleaned_data
		# abc=form_data.get("email")
		# abc2=form_data.get("email")
		# obj=Registrado.objects.create(email=abc,nombre=abc2)
	contexto={
		"mi_formulario":form,
		"titulo":titulo,
	}
	return render(request,"inicio.html",contexto)
# Create your views here.
