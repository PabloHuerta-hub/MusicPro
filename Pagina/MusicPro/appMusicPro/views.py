from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from MusicPro.appMusicPro.serializers import UserSerializer, GroupSerializer, TipoInstrumentoSerializer, CategoriaSerializer, SubCategoriaSerializer, ProductoSerializer
from tienda.models import Tipo_Instrumento, Categoria, SubCategoria, Producto

# Create your views here.

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet) :
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]    

class TipoInstrumentoViewSet(viewsets.ModelViewSet) :
    queryset = Tipo_Instrumento.objects.all()
    serializer_class = TipoInstrumentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CategoriaViewSet(viewsets.ModelViewSet) :
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubCategoriaViewSet(viewsets.ModelViewSet) :
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet) :
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]


