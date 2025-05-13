from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from testapp.serializers import ProductSerializer
from testapp.models import Product
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
class ProductCRUDCBV(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
class CategoriesView(APIView):
    def get(self,request, *args, **kwargs):
        categories=["men's clothing","women's clothing","jewelery","electronics"]
        return Response(categories)
            
            