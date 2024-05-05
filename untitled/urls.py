"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', view.home, name='home'),
                  path('mlp/', view.register, name='register'),
                  path('svm/', view.svm_view, name='svm'),
                  path('echec/', view.echec, name='echec'),
                  path('success/', view.success, name='success'),
                  path('knn/', view.knn_view, name='knn'),
                  path('cart/', view.cart_view, name='cart')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
