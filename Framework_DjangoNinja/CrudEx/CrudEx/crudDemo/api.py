from ninja import Router, Schema
from datetime import date
from testmodels.models import Employee
from django.shortcuts import get_object_or_404

router = Router()

# 05.CRUD - CREATE
# http://127.0.0.1:8000/api/crud/employees
# body : {EmployeeIn}
class EmployeeIn(Schema):
    name:str
    department_id: int = None
    birthdate: date = None

@router.post("/employees")
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict())
    return {"id": employee.id}

# 06.CRUD - Retrieve
# http://127.0.0.1:8000/api/crud/employees?1
class EmployeeOut(Schema):
    id: int
    name:str
    department_id: int = None # 없으면 Null 반환
    birthdate: date = None

@router.get("/employees/{employee_id}", response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

# 07.CRUD - Retrieve List of objects
# http://127.0.0.1:8000/api/crud/employees
from typing import List
@router.get("/employees", response=List[EmployeeOut])
def list_employees(request):
    qs = Employee.objects.all()
    return qs

# 08.CRUD - Update
# http://127.0.0.1:8000/api/crud/employees/1
# body : {EmployeeIn}
@router.put("/employees/{employee_id}")
def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id=employee_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}

# 09.CRUD - Delete
# http://127.0.0.1:8000/api/crud/employees/1
# body : {EmployeeIn}
@router.delete("/employees/{employee_id}")
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return {"success": True}