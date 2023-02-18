from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Owners
from core.serializers import OwnerSerializer

@csrf_exempt
def owners_list(request):
    if request.method == 'GET':
        snippets = Owners.objects.all()
        serializer = OwnerSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def owner_detail(request, pk):
    try:
        owner = Owners.objects.get(pk=pk)
    except Owners.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OwnerSerializer(owner)
        return JsonResponse(serializer.data)    
