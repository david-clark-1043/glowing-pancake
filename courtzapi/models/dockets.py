from django.db import models

class Docket(models.Model):
    case_num = models.CharField(max_length=50)
    case_name = models.CharField(max_length=300, default="tbd")
    status = models.ForeignKey("CaseStatus", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    completed_on = models.DateTimeField(null=True, blank=True)
