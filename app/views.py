from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Employee


class TemplateReturn(TemplateView):
    template_name = 'home.html'


class EmployeeList(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'tiru'


class EmployeeDetailedList(DetailView):
    model = Employee
    template_name = 'detailedlist.html'
    context_object_name = 'tiru'


class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'create_employee.html'
    fields = '__all__'


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'age']
    template_name = 'update.html'


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'delete.html'
    context_object_name = 'tiru'
    success_url = reverse_lazy ('list_view')
