"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from core.util import set_language

from application.views import LoginView, HomeView

import accescontrol.urls

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accescontrol/',include(accescontrol.urls)),
    
    path('',LoginView.as_view(), name='index'),
    path('home',HomeView.as_view(), name='home'), 
    
]

urlpatterns = [
    *i18n_patterns (*urlpatterns,prefix_default_language=False),
     path('set_lenguage',set_language,name='set_language')
     
]

urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
