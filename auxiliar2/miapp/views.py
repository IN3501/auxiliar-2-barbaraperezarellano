from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')

def equipodocente(request):
	return render(request, 'miapp/equipodocente.html')

def seleccion(request):
	return render(request, 'miapp/seleccion.html')
	