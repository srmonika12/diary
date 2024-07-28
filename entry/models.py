from django.db import models
from django.utils import timezone
# Create your models here.
class entry(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    

