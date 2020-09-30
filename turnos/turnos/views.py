from django.shortcuts import render
from .forms import FormularioContacto
from django.core.mail import send_mail

def Home(request):
	if (request.user.is_anonymous):
		return render(request,'home.html')
	else:
		if (request.user.es_duenio):
			return render(request,'homeSesionDuenio.html')
		else:
			return render(request,'homeSesion.html')

def contacto(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			infForm=formulario.cleaned_data 

			send_mail(infForm['asunto'],infForm['mensaje'],
				infForm.get('email',''),['RenzoBalbiano@hotmail.com'],)

			return render(request,'gracias.html')
	else:
		formulario = FormularioContacto()

	return render(request,'contacto.html',{'form': formulario})

def nosotros(request):
	return render(request,'nosotros.html')
