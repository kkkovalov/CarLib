from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cardbAPI.models import Manufacturers, Models
from cardbAPI.serializers import ManufacturerSerializer, ModelSerializer

# Create your views here.
@csrf_exempt
def manufacturerApi(request, id=0):
    if request.method=='GET':
        manufacturers = Manufacturers.objects.all()
        manufacturers_serializer = ManufacturerSerializer(manufacturers, many=True)
        return JsonResponse(manufacturers_serializer.data, safe=False)
    elif request.method=='POST':
        manufacturer_data = JSONParser().parse(request)
        manufacturers_serializer=ManufacturerSerializer(data=manufacturer_data)
        if manufacturers_serializer.is_valid():
            manufacturers_serializer.save()
            return JsonResponse('Successfuly added to the database', safe=False)
        return JsonResponse('Unable to add data', safe=False)
    elif request.method=="PUT":
        pass

    