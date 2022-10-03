import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Brands

# Create your views here.
class BrandsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            brands = list(Brands.objects.filter(id=id).values())
            if len(brands) > 0:
                brand = brands[0]
                datos = {'message': 'success', 'brands': brand}
            else:
                datos = {'message': 'Brands not found'}
            return JsonResponse(datos)
        else:
            brands = list(Brands.objects.values())
            if len(brands) > 0:
                datos = {'message': 'success', 'brands': brands}
            else:
                datos = {'message': 'Brands not found'}
            return JsonResponse(datos)
        

    def post(self, request):
        body = json.loads(request.body)
        Brands.objects.create(name=body['name'])
        datos = {'message': 'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        body = json.loads(request.body)
        brands = list(Brands.objects.filter(id=id).values())
        if len(brands) > 0:
            brand = Brands.objects.get(id=id)
            brand.name = body['name']
            brand.save()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Brand not found'}
        return JsonResponse(datos)

    def delete(self, request, id):
        brands = list(Brands.objects.filter(id=id).values())
        if len(brands) > 0:
            Brands.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Brand not found'}
        return JsonResponse(datos)
