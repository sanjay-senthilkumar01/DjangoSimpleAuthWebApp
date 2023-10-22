from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:

            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, null=True, blank=True)  # Add the company field
    location_experience = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=10, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    school = models.CharField(max_length=100,null=True, blank=True)
    degree = models.CharField(max_length=100,null=True, blank=True)
    field_of_study = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
  

class Website(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_url = models.URLField(null=True, blank=True)
    contributors = models.ManyToManyField(Profile, related_name='contributed_projects',null=True, blank=True)
    associated_with = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)