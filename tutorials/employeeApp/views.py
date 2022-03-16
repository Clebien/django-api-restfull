from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from employeeApp.models import Departments, Employees
from employeeApp.serializers import DepartmentSeralizer, EmployeeSeralizer

from django.core.files.storage import default_storage
# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_seralizer = DepartmentSeralizer(departments, many=True)
        return JsonResponse(departments_seralizer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_seralizer = DepartmentSeralizer(data=department_data)
        if departments_seralizer.is_valid():
            departments_seralizer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_seralizer = DepartmentSeralizer(department, data=department_data)
        if departments_seralizer.is_valid():
            departments_seralizer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def empployeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_seralizer = EmployeeSeralizer(employees, many=True)
        return JsonResponse(employees_seralizer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_seralizer = EmployeeSeralizer(data=employee_data)
        if employees_seralizer.is_valid():
            employees_seralizer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        emplyees_seralizer = EmployeeSeralizer(employee, data=employee_data)
        if emplyees_seralizer.is_valid():
            emplyees_seralizer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FLIES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
