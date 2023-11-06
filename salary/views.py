from django.shortcuts import render
from salary.models import Employee
from django.shortcuts import get_object_or_404
# Create your views here.
def details(requist,pk):
    employee=get_object_or_404(Employee,pk=pk)
    context={
        'employee':employee
    }
    return render(requist,'details.html',context)