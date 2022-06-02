from django.db import models

class FilingType(models.Model):
    filing_type = models.CharField(max_length=50)
