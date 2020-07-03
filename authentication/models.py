from django.db import models


# Create your models here.
class MMAR(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ngc_path = models.CharField(max_length=255)
    version = models.IntegerField(default=1)
    downloaded_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
