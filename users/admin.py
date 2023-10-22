from django.contrib import admin
from .models import Profile , Website , Project , Experience , Education

# Register your models here.
admin.site.register(Profile)
admin.site.register(Website)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Education)