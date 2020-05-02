from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import Cat
from .serializers import CatSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

# Create your views here.

def CatsList(request, *args, **kwargs):
    per_page = request.GET.get('per_page')

    queryset = Cat.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    paginator = Paginator(queryset, per_page or 5)
    serializer_class = CatSerializer
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    serializer = serializer_class(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)
