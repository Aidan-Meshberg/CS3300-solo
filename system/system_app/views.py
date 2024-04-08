from django.shortcuts import render, redirect
from django.http import HttpResponse
from system_app.models import *
from django.views import generic
from system_app.forms import *


def index(request):
   perDiems = Per_Diem.objects.select_related('per_diem').all()
   print("Per Diem set", perDiems)
   return render( request, 'system_app/index.html', {'perDiems':perDiems})

class WorkerListView(generic.ListView):
   model = Worker

class WorkertDetailView(generic.DetailView):
   model = Worker


def system_details(request):
   diem_id = request.GET.get('button_id')
   diem = Per_Diem.objects.get(id = diem_id)
   projects = Day_to_Day.objects.all().filter(perdiem_id = diem_id)
   return render(request, 'system_app/port_details.html', {'port': diem, 'projects': projects})


def add_day(request):
    diem_id = request.GET.get('button_id')

    if request.method == 'POST':
        form = AddDay(request.POST)
        if form.is_valid():
            newProject = form.save(commit = False)
            newProject.perdiem_id = diem_id
            newProject.save()

            url = request.session.pop('current_url', '/') + 'port_details?button_id=' + diem_id

            return redirect(url)
    else:
        form = AddDay()
    return render(request, 'system_app/add_project.html', {'form': form})



def update_project(request):
   diem_id = request.GET.get('diem_id')
   day_id = request.GET.get('day_id')
   day = Day_to_Day.objects.get(id = day_id)

   if request.method == 'POST':
        form = AddDay(request.POST)
        if form.is_valid():
            newProject = form.save(commit = False)
            newProject.perdiem_id = diem_id
            newProject.save()

            url = request.session.pop('current_url', '/') + 'port_details?button_id=' + diem_id

            return redirect(url)
   else:
        form = AddDay()
   return render(request, 'system_app/add_project.html', {'form': form})



def delete_day(request):
   diem = request.GET.get('diem')
   day_id = request.GET.get('day_id')
   day = Day_to_Day.objects.get(id = day_id)
   return render(request, 'system_app/delete_project.html', {'project': day, 'port': diem})



def delete_day_cancel(request):
   diem = request.GET.get('diem')
   day_id = request.GET.get('day_id')
   day = Day_to_Day.objects.get(id = day_id)

   url = request.session.pop('current_url', '/') + 'system_details?button_id=' + diem
   return redirect(url)



def delete_day_confirm(request):
   diem = request.GET.get('diem')
   day_id = request.GET.get('projects_id')
   day = Day_to_Day.objects.get(id = day_id)

   day.delete()

   url = request.session.pop('current_url', '/') + 'system_details?button_id=' + diem
   return redirect(url)



def view_day(request):
    diem = request.GET.get('diem_id')
    day_id = request.GET.get('projects_id')
    day = Day_to_Day.objects.get(id = day_id)
    return render(request, 'system_app/view_day.html', {'project': day_id})



def worker_list(request):
    worker = Worker.objects.all()
    return render(request, 'system_app/worker_list.html', {'student': worker})



def worker_detail(request):
   worker_id = request.GET.get("workwe_id")
   worker = Worker.objects.get(id = worker_id)
   diem = Per_Diem.objects.get(id = worker.per_diem_id)
   return render(request, 'system_app/worker_detail.html', {'student': worker, 'port': diem})



def update_diem(request):
   diem_id = request.GET.get('diem_id')
   worker_id = request.GET.get('worker_id')
   diem = Per_Diem.objects.get(id = diem_id)

   if request.method == 'POST':
      form = updateDiem(request.POST, instance=diem)
      if form.is_valid():
         form.save()

         url = request.session.pop('current_url', '/') + 'per_diem_details?button_id=' + worker_id
         return redirect(url)
      
   else: 
      form = updateDiem(instance=diem)
   return render(request, 'system_app/update_diem.html', {'form': form})