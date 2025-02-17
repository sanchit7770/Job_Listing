from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('positionName', 'company', 'location', 'salary', 'postedAt')  # ✅ Use valid fields from Job model

admin.site.register(Job, JobAdmin)

