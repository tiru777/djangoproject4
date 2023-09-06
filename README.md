```commandline
Check project Intial steps in previous repo
```

```commandline
Class Based Views
```

```commandline
- After installing Django project and configuration
- Create Templates folder and configure in Settings.py file
- create static folder and configure in settings.py file
```

```commandline
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

Class Based View
   => Template View
          - for returning html file using template_name = html_file
   => List View
          - for returning list we have to mention model name and context object name and template_name
          - configure views in urls.py file and mention url name 
          - Display list of data in html using for loop
            - {% for i in context_object_name%} {{i.field_name}} {% endfor %}
            - if you want make url for detailed view for each object 
                - <a href="{% url 'detailed_view' i.pk %}"> Detailed View</a>
            - if you want to update specific field 
                - <a href="{% url 'update_view' i.pk %}"> Update View</a>
           
  => Detailed View
      - for returning Detailed view of each object, we have to mention model name and context object name and template_name
      - configure views in urls.py file and mention url name, 
      - path('detail/<int:pk>/', EmployeeDetailedList.as_view(), name='detailed_view'), 
      - Display list of data in html using for loop
      - {{contaxt_object.field_name}}
      
  => Create View
       - for creating fields based on model, we have to mention model name
       - then we have to mention template_name 
       - Then we have to mention fields, what fields we need
       - html file body in Form we have to mention   {% csrf_token %}  {{form.as_p}} and type submit 
       - after submitting we have to redirect other page for that we have to mention in models
            - def get_absolute_url(self): return "/ur_name"
  => Update View
       - For updating specific object we need specific id for that either you have id number or specific id from list
       - path('update/<int:pk>/', EmployeeUpdate.as_view(), name='update_view'),
       - we have to mention model name,fields to update and template name 
       - html file body in Form we have to mention   {% csrf_token %}  {{form.as_p}} {{object.fields}}and type submit value update
  => Delete View
       - For deleting specific object we need specific id for that either you have id number or specific id from list
       -     path('delete/<int:pk>/', EmployeeDelete.as_view(), name='delete_view'),
       - we have to mention model name,template name,contex_object_name, success_url = reverse_lazy ('list_view'),here list_view is name of url
       - html file body in Form we have to mention   {% csrf_token %}  {{form.as_p}} {{object.fields}} and type submit value confirm
       - after deleting successfully it will redirecting to reverse lazy url

```