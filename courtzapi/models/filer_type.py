from django.db import models

# Filer type goes with the filer itself
# can be pro se, party, attorney, other representative, judge, clerk

class FilerType(models.Model):
    filer_type = models.CharField(max_length=50)
