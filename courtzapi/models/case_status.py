from django.db import models

class CaseStatus(models.Model):
    status_label = models.CharField(max_length=50)
