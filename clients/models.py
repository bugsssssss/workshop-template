from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(
        User, verbose_name=_("client"), on_delete=models.CASCADE
    )
    company_name = models.CharField(_("company name"), max_length=100)
    full_address = models.CharField(_("full address"), max_length=100)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.user.username
