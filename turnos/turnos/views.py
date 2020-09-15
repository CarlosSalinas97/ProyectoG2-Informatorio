from django.shortcuts import render
from .forms import FormularioContacto
from django.core.mail import send_mail

def Home(request):
	return render(request,'home.html')

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
