from django.contrib import admin

# Register your models here.

from .models import Per_Diem
from .models import Worker
from .models import Day_to_Day

admin.site.register(Per_Diem)
admin.site.register(Worker)
admin.site.register(Day_to_Day)