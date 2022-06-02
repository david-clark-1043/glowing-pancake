from django.db import models

class DocketFilers(models.Model):
    docket = models.ForeignKey("Docket", on_delete=models.CASCADE)
    filer = models.ForeignKey("Filer", on_delete=models.CASCADE)
