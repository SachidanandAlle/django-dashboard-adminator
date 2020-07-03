from django.db import models


class MMAR(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ngc_path = models.CharField(max_length=255)
    version = models.IntegerField(default=1)
    downloaded_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=255, null=True)

class Dataset(models.Model):
    name = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=255)
    is_gdrive = models.BooleanField(default=False)
    downloaded_at = models.DateTimeField(null=True)
    description = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
