"""project42 URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app42 import views
from project42 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowIndex.as_view(),name='main'),
    #path('add_employee/',TemplateView.as_view(template_name='employee.html'),name='add_employee'),
    path('add_employee/',views.AddEmployee.as_view(),name='add_employee'),
    path('view_all_employee/',views.ViewAllEmployee.as_view(),name='view_all_employee'),
    path('view_employee/',views.ViewEmployee.as_view(),name='view_employee'),
    path('completeview/<int:pk>',views.CompleteView.as_view(),name='completeview'),
    path('update_value/<int:pk>',views.UpdateValue.as_view(),name='update_value'),
    path('delete_value/<int:pk>',views.DeleteValue.as_view(),name='delete_value'),
    path('search_employee/',views.SearchEmployee.as_view(),name='search_employee'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
