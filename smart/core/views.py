from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from core.models import Companies, Users, Analytic, Action
from core.serializers import CompaniesSerializer, UsersSerializer, AnalyticSerializer, ActionSerializer
from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


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
    

def analytics_list(request):
    if request.method == 'GET':
        snippets = Analytic.objects.all()
        serializer = AnalyticSerializer(snippets, many=True)
        data = {'data': serializer.data}
        return JsonResponse(data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnalyticSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse([serializer.data], status=201)
        return JsonResponse(serializer.errors, status=400)
    

def analytics_detail(request, name):
    try:
        owner = Analytic.objects.get(name=name)
    except Analytic.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnalyticSerializer(owner)
        return JsonResponse([serializer.data]) 
    

def action_list(request):
    if request.method == 'GET':
        snippets = Action.objects.all()
        serializer = ActionSerializer(snippets, many=True)
        data = serializer.data
        return JsonResponse(data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    

def action_detail(request, name):
    try:
        owner = Action.objects.get(name=name)
    except Action.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActionSerializer(owner)
        return JsonResponse(serializer.data)
    

class AnalyticViewSet(viewsets.ModelViewSet):
    queryset = Analytic.objects.all()
    serializer_class = AnalyticSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
