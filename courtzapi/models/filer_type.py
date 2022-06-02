from django.db import models

class FilerType(models.Model):
    filer_type = models.CharField(max_length=50)
