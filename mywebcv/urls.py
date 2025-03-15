from django.contrib import admin
from django.urls import path, include
from backoffice import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('home.urls')),
]

#Backoffice
urlpatterns += [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='register.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('backoffice/', views.backoffice, name='backoffice'),
    path('backoffice/add_certificate/', views.add_certificate, name='add_certificate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)