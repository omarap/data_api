"""data_collection_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/analysis/', include('analysis.urls')),
    path('api/pandas_analysis/', include('pandas_analysis.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # new
    path('api/v1/dj-rest-auth/registration/', 
                    include('dj_rest_auth.registration.urls'), name='registration') # new

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

