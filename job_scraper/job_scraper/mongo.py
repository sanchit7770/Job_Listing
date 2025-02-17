import pymongo
import numpy as np
import re

# Connect to MongoDB (replace with your actual connection string)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_database"]  # Replace with your DB name
collection = db["jobs"]      # Replace with your collection name

# Fetch all job listings
jobs = collection.find({}, {"salary": 1, "_id": 0})

# Extract numeric salary values
salaries = []

for job in jobs:
    if "salary" in job and job["salary"]:
        # Extract numeric values from salary string (e.g., "₹50,000 - ₹60,000/month")
        salary_numbers = re.findall(r'\d+', job["salary"])
        if salary_numbers:
            avg_salary = np.mean(list(map(int, salary_numbers)))
            salaries.append(avg_salary)

# Calculate average salary
if salaries:
    avg_salary = np.mean(salaries)
    print(f"Average Python Developer Salary: ₹{avg_salary:,.2f}")
else:
    print("No salary data available.")
