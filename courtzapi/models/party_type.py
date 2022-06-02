from django.db import models

class PartyType(models.Model):
    party_type = models.CharField(max_length=50)
