from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib import messages
from .models import Comuna
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.

#funcion para devolver las columnas en funcion de la region seleccionada
def get_comunas(request):
    id_region = request.GET.get('region')
    try:
        comunas = Comuna.objects.filter(cod_provincia__cod_region_id=id_region)
        data = []
        for i in comunas:
            data.append({'id': i.id, 'comuna': i.nombre})
    except Exception as e:
        data['error'] =str(e)
    return JsonResponse(data, safe=False)

class IndexView(TemplateView):
    template_name = 'index.html'

index_view = IndexView.as_view()

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        if not request.POST.get('remember_me'):
            request.session.set_expiry(0)
            #Authenticamos con usuario o correo
        user = authenticate(request, username=username_or_email, email=username_or_email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.first_name}!')
            return redirect('property:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'pagetitle': 'Iniciar sesión'})     

