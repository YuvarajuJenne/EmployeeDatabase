from django.shortcuts import render
from salary.models import Employee
def home(requist):
    employees=Employee.objects.all()
    context={
        'employees':employees
    }
    return render(requist,'index.html',context)