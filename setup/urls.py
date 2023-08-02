# usar include para incluir arquivo com a lista de URL's por App#


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))
    #passar os parâmetros incluídos no settings.py acerca do config de mídia
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
