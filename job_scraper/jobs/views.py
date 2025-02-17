import numpy as np
from django.shortcuts import render
from .models import Job
import re

def job_listings(request):
    jobs = Job.objects.all()  
    return render(request, 'jobs.html', {'jobs': jobs})  

def extract_salary(salary_text):
    if not salary_text:
        return None  

    
    salary_text = salary_text.replace(',', '')  
    numbers = re.findall(r'\d+', salary_text)

    if numbers:
        return int(numbers[0])  
    return None  

def calculate_average_salary(request):
    """Calculate the average salary for Python developers."""
    jobs = Job.objects.exclude(salary="Not Disclosed")  
    salaries = [extract_salary(job.salary) for job in jobs if extract_salary(job.salary) is not None]

    if salaries:
        avg_salary = np.mean(salaries) 
        avg_salary=round(avg_salary,3) 
    else:
        avg_salary = 0  

    return render(request, 'average_salary.html', {'average_salary': avg_salary})
