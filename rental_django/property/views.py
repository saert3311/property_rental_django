from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from django.shortcuts import redirect

# Create your views here.
@login_required
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
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
    return render(request, 'property/add.html', {'form': form, 'pagetitle': 'Agregar propiedad'})