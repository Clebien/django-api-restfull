from django.urls import re_path
from employeeApp import views



urlpatterns=[
    re_path(r'^department/$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),

    re_path(r'^employee/$', views.empployeeApi),
    re_path(r'^employee/([0-9]+)$', views.empployeeApi),
]