# serializers.py
# Aqui vamos a definir que campos vamos a mostrar
# para cada modelo.
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tienda.models import Tipo_Instrumento, Categoria, Producto, SubCategoria
        
class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Group
        fields = ['url', 'name']


class TipoInstrumentoSerializer(serializers.HyperlinkedModelSerializer) :

    class Meta:
        model = Tipo_Instrumento
        fields = ['nombre']

class CategoriaSerializer(serializers.HyperlinkedModelSerializer) :
    tipo_instrumento = TipoInstrumentoSerializer(read_only=True)
    tipo_instrumentoId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tipo_Instrumento.objects.all(), source='tipo_instrumento')
    class Meta:
        model = Categoria
        fields = ['nombre', 'tipo_instrumento', 'tipo_instrumentoId']

class SubCategoriaSerializer(serializers.HyperlinkedModelSerializer) :
    categoria = CategoriaSerializer(read_only=True)
    categoriaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='categoria')
    class Meta:
        model = SubCategoria
        fields = ['nombre', 'categoria', 'categoriaId']

class ProductoSerializer(serializers.HyperlinkedModelSerializer) :
    sub_categoria = SubCategoriaSerializer(read_only=True)
    sub_categoriaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SubCategoria.objects.all(), source='sub_categoria')
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'precio', 'serie_producto', 'marca', 'sub_categoria', 'sub_categoriaId']