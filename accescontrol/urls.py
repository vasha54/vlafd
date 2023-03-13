from django.contrib import admin
from django.urls import path, include

from accescontrol.views import changeStatusUsserAccesControl



urlpatterns = [
   path('changestatus/<usuario_id>',changeStatusUsserAccesControl,name='changeStatus'),
]