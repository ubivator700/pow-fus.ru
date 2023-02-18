from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Companies, Users, Analytic
from core.serializers import CompaniesSerializer, UsersSerializer, AnalyticSerializer

@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        snippets = Users.objects.all()
        serializer = UsersSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):
    try:
        owner = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersSerializer(owner)
        return JsonResponse(serializer.data)    
    

def companies_list(request):
    if request.method == 'GET':
        snippets = Companies.objects.all()
        serializer = CompaniesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CompaniesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

def company_detail(request, pk):
    try:
        owner = Companies.objects.get(pk=pk)
    except Companies.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CompaniesSerializer(owner)
        return JsonResponse(serializer.data) 
    

def analytic(request):
    try:
        analytic = Analytic.objects.all()
    except Analytic.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AnalyticSerializer(analytic)
        return JsonResponse(serializer.data)
