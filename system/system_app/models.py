from django.db import models
from django.urls import reverse


class Per_Diem(models.Model):
    title = models.CharField(max_length=200, default="Title")
    about = models.TextField(blank = True)
    contact_email = models.CharField(max_length=200, blank = True)
    phone_number = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class Worker(models.Model):
#list of worker types
    TITLE = (
    ('Satalite truck opperator'),
    ('Producer'),
    ('On site tech')
    )
    name = models.CharField(max_length=200)
    email = models.CharField("Company Email", max_length=200)
    title = models.CharField(max_length=200, choices=TITLE, blank = True)
    per_diem = models.OneToOneField(Per_Diem, null=True, on_delete=models.CASCADE, unique=True)
    

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name


    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
    

class Day_to_Day(models.Model):
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    money_spent = models.CharField(max_length=200, null = True)
    per_diam = models.ForeignKey(Per_Diem, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])