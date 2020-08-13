"""brocode URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    path('',  include('main.urls', namespace="app_name",)),
    path('', include('payment.urls')),
    path('admin/', admin.site.urls),
    path('subscribe/', include('subscribe.urls')),

    # path(r'^$', ChatterBotAppView.as_view(), name='main'),
    # path(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)