from django.contrib import admin
from boletin.models import Registrado
from boletin.forms import RegModelForm
# Register your models here

admin.site.register(Registrado)
class AdminRegistrado(admin.ModelAdmin):
	list_display=["email","nombre","timestamp"]
	form=RegModelForm
	list_editable=["nombre"]
	search_fields=["email","nombre"]
	

