from http.client import HTTPResponse
from django.shortcuts import render
from mysite.models import Employee
from mysite import views


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        doj = request.POST.get('doj')
        deadline =  request.POST.get('deadline')
        
        employee = Employee (
            name = name,
            DOJ = doj,
            deadline = deadline,
            

        )
        employee.save()
    return render(request, 'home.html')





