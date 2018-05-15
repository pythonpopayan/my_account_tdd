"""dj_myaccount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from persons import views as persons_views

urlpatterns = [
    path('dashboard/', persons_views.dashboardTemplateView.as_view(), name='dashboard'),
    path('detail/<slug:category>/', persons_views.detailTemplateView.as_view(), name='detail'),
    # path('settings/', persons_views.settingsTemplateView.as_view(), name='settings'),
    # path('dump-balance/', persons_views.dumpBalanceTemplateView.as_view(), name='dump-balance'),

]
