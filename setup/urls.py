# usar include para incluir arquivo com a lista de URL's por App#


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
]
