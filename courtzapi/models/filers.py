from django.db import models
from django.contrib.auth.models import User


class Filer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    state_code = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_num = models.CharField(max_length=10)
    firms = models.ManyToManyField("Firm", through="RepFirm", related_name="representatives")
    representation = models.ManyToManyField("RepFirm", through="RepFirmParty", related_name="clients")
    filer_type = models.ForeignKey("FilerType", on_delete=models.CASCADE)
    # managing_dockets = models.ManyToManyField("Docket", through="DocketFilers", related_name="managers")
