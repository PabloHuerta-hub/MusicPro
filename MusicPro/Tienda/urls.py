from django.urls import path,include,re_path
from .views import index,contact,blog,product,about
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
   path('',index, name='Index'),
   path('contactanos',contact, name='Contactanos'),
   path('blog',blog,name='Blog'),
   path('productos',product,name='Product'),
   path('sobrenuestrosproductos',about,name='About'),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)