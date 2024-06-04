from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import PropertyForm, RequestForm, UpdatePropertyForm
from .models import Property, Request, Contract
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

# Create your views here.
@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.landlord = request.user
            obj.save()
            messages.success(request, 'Propiedad publicada exitosamente.')
            return redirect('users:dashboard')
        else:
            #get form errors and append to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')

    form = PropertyForm()
    return render(request, 'property/add.html', {'form': form, 'pagetitle': 'Agregar propiedad', 'action': 'Agregar'})


def property_details(request, id):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.origin_property = get_object_or_404(Property, pk=id)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Solicitud enviada exitosamente.')
            return redirect('users:index')
        else:
            #get form errors and append to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    data = {}
    property_data = get_object_or_404(Property, pk=id)
    data['pagetitle'] = property_data.name
    data['property_data'] = property_data
    if request.user == property_data.landlord:
        data['requests'] = Request.objects.filter(origin_property=id).order_by('-created')
        data['contracts'] = Contract.objects.filter(origin_request__origin_property=id)
    if request.user.is_authenticated and request.user != property_data.landlord:
        data['request_form'] = RequestForm()        
        data['has_contacted'] = property_data.user_has_request(request.user)    
    return render(request, 'property/show.html', data)

class PropertyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Property
    form_class = UpdatePropertyForm
    template_name = 'property/update.html'
    success_url = '/dashboard/'
    success_message = 'Propiedad actualizada exitosamente.'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagetitle'] = 'Actualizar propiedad'
        context['action'] = 'Actualizar'
        return context
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.landlord != self.request.user:
            raise PermissionDenied
        return obj

