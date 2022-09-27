from django.contrib import admin
from django.urls import path
from untirta.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('untirta/',index),
]
