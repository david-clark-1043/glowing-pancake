from django.db import models

# party type goes on the docket party bridge table
# options currently are plaintiff, defendant, manager, intervenor

class PartyType(models.Model):
    party_type = models.CharField(max_length=50)
