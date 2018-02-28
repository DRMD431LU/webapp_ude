from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import RegModelForm,ContactForm
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
			"titulo":"Gracias %s!"%(nombre),
		}
		if not nombre:
			contexto={
				"titulo":"Gracias %s!"%(email),
			}
		print (instance)
		print(instance.timestamp)
		# form_data=form.cleaned_data
		# abc=form_data.get("email")
		# abc2=form_data.get("email")
		# obj=Registrado.objects.create(email=abc,nombre=abc2)
	return render(request,"inicio.html",contexto)

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		# for key,value in form.cleaned_data.items():
		# 	print(key,value)
		# for key in form.cleaned_data:
		# 	print(key)
		# 	print(form.cleaned_data.get(key))
		email=form.cleaned_data.get("email")
		mensaje=form.cleaned_data.get("mensaje")
		nombre=form.cleaned_data.get("nombre")
		asunto='Form de contacto'
		from_email=settings.EMAIL_HOST_USER
		recipient_list=[from_email,"mail@mail.com"]
		email_mensaje= "%s: %s enviado por %s" %(nombre, mensaje, email)
		send_mail(asunto, email_mensaje, from_email, recipient_list,fail_silently=False)
		# print(email,mensaje, nombre)
	context={
	"form":form
	}
	return render(request,"forms.html",context)