from django.urls import path
from employee.views import employee_list

urlpatterns = [path('all', employee_list, name="emps.all" )]
