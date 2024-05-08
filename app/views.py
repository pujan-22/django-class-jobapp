from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from django.urls import reverse
from app.models import JobPost

# Create your views here.
job_title = [
    '',
    'Job Title 1', 'Job Title 2', 'Job Title 3'
]

job_desc = [
    '','Description 1', 'Description 2', 'Description 3'
]

class TempClass:
    a = 10

def hello(request):
    # template = loader.get_template('app/hello.html')
    list = ["a value", "second value"]
    is_loggedin = True
    temp_class = TempClass()
    context = {"user" : "Pujan", "list" : list, "temp_class" : temp_class, "age" : "21", "is_loggedin" : is_loggedin}
    return render(request, "app/hello.html", context)

def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs" : jobs}
    return render(request, "app/index.html", context)

def job_detail(request, id):
    try:        
        if id == 0:
            return redirect(reverse("job_list"))
        job = JobPost.objects.get(id=id)
        context = {"job":job}
        return render(request, "app/job_detail.html", context)
    except JobPost.DoesNotExist:
        return HttpResponseNotFound("Not Found")