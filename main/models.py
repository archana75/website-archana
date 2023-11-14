from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Generation(models.Model):
    name = models.CharField(max_length=100)
    school_year = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.school_year} - {self.name}"

class Student(models.Model):
    nisn = models.CharField(max_length=10)
    nis = models.CharField(max_length=10)
    firstname = models.CharField (max_length=100)
    lastname = models.CharField (max_length=100)
    is_active = models.BooleanField(default=True)
    generation = models.ForeignKey(
        Generation,
        on_delete=models.CASCADE
                )
    
    def __str__(self):
        return f"{self.nisn} - {self.firstname} {self.lastname}"
    
class Post(models.Model):
    image = models.ImageField(upload_to='images')
    caption = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE,
                    blank=True, null=True
                )

class Event(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    is_published = models.BooleanField(default=True)
    attachment_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE,
                )

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    logo = models.ImageField(upload_to='images', blank=True)
    video_link = models.URLField(blank=True)
    attachment_link = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    school_product = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    Student,
                    on_delete=models.CASCADE,
                )

class Achievement(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ManyToManyField(Project)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    Student,
                    on_delete=models.CASCADE,
                ) 
    
    def __str__(self):
        return f"{self.id} - {self.event_name}"
    
class AchievementPhoto(models.Model):
    photo = models.ImageField(upload_to='images')
    achievement = models.ForeignKey(
                    Achievement,
                    on_delete=models.CASCADE
                )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    Student,
                    on_delete=models.CASCADE
                )
    
class Cms(models.Model):
    name = models.CharField(unique=True, max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE
                )
    
    class Meta:
         verbose_name = "CMS"
