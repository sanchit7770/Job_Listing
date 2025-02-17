from djongo import models

class Job(models.Model):
    salary = models.CharField(max_length=100, null=True)
    postedAt = models.CharField(max_length=50)
    externalApplyLink = models.URLField()
    positionName = models.CharField(max_length=200)
    jobType = models.JSONField()  # List of job types
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    reviewsCount = models.IntegerField()
    url = models.URLField()
    description = models.TextField()
    
    class Meta:
        db_table = "jobs"