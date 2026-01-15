from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

     path('clients/', ClientListCreateView.as_view(), name="client_endpoint"),
     path('clients/<int:pk>/', ClientRetreiveUpdateDeleteView.as_view(), name="client_detail_endpoint"),

]
