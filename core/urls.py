from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('paciente/', include('paciente.urls')),
    path('profissional/', include('profissional.urls')),
    path('agenda/', include('agenda.urls')),
    path('registros/', include('registros.urls')),
    
]
