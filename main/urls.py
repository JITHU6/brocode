from django.urls import path

# importing views from views..py
from . import views


app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='index'),
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('blog/', views.blog, name='blogs'),
    # path('blog/<slug:slug>', views.blogdetails, name='blogdetails'),
    # path('blogdetails//<slug:slug>', views.blogdetails, name='blog'),
]