from django.urls import path
from django.contrib import admin
from .views import job_listings
from .views import calculate_average_salary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', job_listings, name='job_listings'), 
    path('jobs/average-salary/', calculate_average_salary, name='average_salary'),
]
