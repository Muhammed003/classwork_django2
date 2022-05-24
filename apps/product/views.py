from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import Products, Category
from .serializers import CategorySerializers



class CategoryListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = CategorySerializers


class PostDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

def index(request):
    category = Category.objects.all()
    return render(request, 'index.html', {'category': category})


def get_product(request, slug):
    category = Category.objects.all()
    products = Products.objects.filter(category__slug=slug)
    return render(request, 'product.html', {'products': products, 'category': category})
