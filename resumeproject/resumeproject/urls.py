from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('', include("serv.urls")),
    path('', include("edu.urls")) ,
    path('', include("contact.urls")) ,
]
