from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('system_details', views.system_details, name='system_details'),
path('add_day', views.add_day, name='add_day'),
path('update_diem', views.update_diem, name='update_diem'),
path('delete_day', views.delete_day, name='delete_day'),
path('delete_day_cancel', views.delete_day_cancel, name='delete_day_cancel'),
path('delete_day_confirm', views.delete_day_confirm, name='delete_day_confirm'),
path('view_day', views.view_day, name = 'view_day'),
path('worker_detail', views.worker_detail, name='worker_detail'),
path('worker_list', views.worker_list, name='worker_list'),
path('update_day', views.update_day, name='update_day')
]
