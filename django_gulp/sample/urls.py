from django.urls import path

from . import views

app_name = "outbound"

from . import views

app_name = "sample"

urlpatterns = [
        path('detail/', views.sample, name='detail'),
        ]
