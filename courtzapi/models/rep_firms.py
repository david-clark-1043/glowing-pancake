from django.db import models

class RepFirm(models.Model):
    representative = models.ForeignKey("Filer", on_delete=models.CASCADE)
    firm = models.ForeignKey("Firm", on_delete=models.CASCADE)
