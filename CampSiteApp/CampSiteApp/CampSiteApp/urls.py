"""CampSiteApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.campsite_home, name='CampSite_home'),
    path('add_campsite/', views.add_campsite, name='add_campsite'),
    path('browse_campsites/', views.browse, name='browse'),
    path('campsite_details/<int:campsite_id>/', views.campsite_details, name='campsite_details'),
    path('campsite_details/<int:campsite_id>/edit', views.edit_campsite, name='edit_campsite'),
    path('campsite_details/<int:campsite_id>/delete', views.delete_campsite, name='delete_campsite'),
    path('CampSite_nationalForest/', views.bs_scrape, name='nationalForest'),
    path('CampSite_searchAPI/', views.search_api, name='searchAPI'),
]
