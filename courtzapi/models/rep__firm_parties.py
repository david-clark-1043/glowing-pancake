from django.db import models

class RepFirmParty(models.Model):
    rep_firm = models.ForeignKey("RepFirm", on_delete=models.CASCADE)
    party = models.ForeignKey("Filer", on_delete=models.CASCADE)