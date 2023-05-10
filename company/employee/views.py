from django.shortcuts import render
from employee.models import Employee 
# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee/employees.html", {"emps":employees})
    

