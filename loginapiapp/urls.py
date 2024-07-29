from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'login', LogInViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login_form/', views.login_view, name='login'),
    path('success/', views.success_page, name='success_page'),
]
