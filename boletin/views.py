from django.shortcuts import render
from .forms import RegForm,RegModelForm
from .models import Registrado
def inicio(request):
	titulo="hola"
	if request.user.is_authenticated():
		titulo="bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	contexto={
		"mi_formulario":form,
		"titulo":titulo,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		nombre=form.cleaned_data.get("nombre")
		email=form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre="PERSONA"
		instance.save()
		contexto={
			"titulo":"Gracias %s!"%(nombre)
		}
		print (instance)
		print(instance.timestamp)
		# form_data=form.cleaned_data
		# abc=form_data.get("email")
		# abc2=form_data.get("email")
		# obj=Registrado.objects.create(email=abc,nombre=abc2)
	return render(request,"inicio.html",contexto)

