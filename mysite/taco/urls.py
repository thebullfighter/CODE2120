from django.conf.urls import url, include
from django.urls import path
from . import views

#this is the name of a function
urlpatterns = [
	path('admin/', admin.site.urls),
    path(r'example/', include('example.urls')),
    path(r'taco', include('taco.urls')),
]
