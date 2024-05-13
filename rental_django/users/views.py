#from django.shortcuts import render
from django.http import JsonResponse
from .models import Comuna

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