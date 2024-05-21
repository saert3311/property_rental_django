from django.shortcuts import get_object_or_404
from django.forms import ValidationError
from django.http import JsonResponse
from django.contrib import messages
from .models import Comuna, UserData
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
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

    def get_context_data(self):
        context = super().get_context_data()
        context["pagetitle"] = 'Inicio'
        return context
    

index_view = IndexView.as_view()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('users:index')
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
            return redirect('users:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'pagetitle': 'Iniciar sesión'})     

def register_view(request):
    if request.user.is_authenticated:
        return redirect('users:index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                data = form.cleaned_data
                user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'], first_name=data['f_name'], last_name=data['l_name'])
                UserData.objects.create(user=user, rut=data['rut'], address=data['address'], phone=data['phone'])
                messages.success(request, 'Usuario creado exitosamente.')
                return redirect('users:login')
        except ValidationError as e:
            for message in e.messages:
                messages.error(request, message)
            return redirect('users:register')
    form = RegisterForm()
    return render(request, 'register.html', {'form':form, 'pagetitle':'Registro'})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('users:index')

@login_required
def dashboard_view(request):
    extra_user_data = UserData.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'pagetitle':'Dashboard', 'extra_user_data':extra_user_data})


@login_required
def edit_profile_view(request):
    extra_user_data = get_object_or_404(UserData, user=request.user)
    password_form = PasswordChangeForm(request.user, request.POST or None)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if 'update_profile' in request.POST and user_form.is_valid():
            user_form.save()
            data = user_form.cleaned_data
            extra_user_data.address = data['address']
            extra_user_data.phone = data['phone']
            extra_user_data.save()
            request.user = User.objects.get(id=request.user.id)
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('users:dashboard')
        elif 'change_password' in request.POST:
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user) 
                messages.success(request, 'Contraseña actualizada exitosamente.')
                return redirect('users:dashboard')
            else:
                #add form errors to messages
                for field, errors in password_form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    user_form = UserUpdateForm(instance=request.user, initial={
        'address': extra_user_data.address,
        'phone': extra_user_data.phone,
    })

    return render(request, 'profile.html', {
        'pagetitle':'Perfil', 
        'user_form': user_form, 
        'password_form': password_form, 
        'extra_user_data': extra_user_data
    })