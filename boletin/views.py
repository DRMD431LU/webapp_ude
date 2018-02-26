from django.shortcuts import render
from .forms import RegForm,ModelRegForm
from .models import Registrado
def inicio(request):
	titulo="Hola"
	if request.user.is_authenticated():
		titulo="Bienvenido %s" %(request.user)
	form=ModelRegForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

		# form_data=form.cleaned_data
		# abc=form_data.get("email")
		# abc2=form_data.get("nombre")
		# obj=Registrado.objects.create(email=abc,nombre=abc2)
	contexto={
		"titulo":titulo,
		"abc":abc,
		"mi_formulario":form,
	}
	return render(request,"inicio.html",contexto)
# Create your views here.
