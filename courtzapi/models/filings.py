from django.db import models

class Filing(models.Model):
    filer = models.ForeignKey("Filer", on_delete=models.CASCADE)
    docket = models.ForeignKey("Docket", on_delete=models.CASCADE, related_name="filings")
    title = models.CharField(max_length=300, default="tbd")
    docket_index = models.IntegerField()
    filed_on = models.DateTimeField(auto_now_add=True)
    filing_type = models.ForeignKey("FilingType", on_delete=models.CASCADE)
    file_url = models.CharField(max_length=100)
    file_pdf = models.FileField(upload_to='caseFiles', default="")
