from django.db import models

class DocketParty(models.Model):
    party = models.ForeignKey("Filer", on_delete=models.CASCADE)
    docket = models.ForeignKey("Docket", on_delete=models.CASCADE, related_name="parties")
    party_type = models.ForeignKey("PartyType", on_delete=models.CASCADE)
