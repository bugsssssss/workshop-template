from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class Service(models.Model):
    name = models.CharField(("name"), max_length=50)
    full_price = models.PositiveIntegerField(("full price"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.name


class Plan(models.Model):
    PLAN_TYPES = (
        ("full", "Full"),
        ("student", "Student"),
        ("discount", "Discount"),
    )

    plan_type = models.CharField(("plan type"), choices=PLAN_TYPES, max_length=10)
    discount_percent = models.PositiveIntegerField(
        ("discount"), validators=[MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plans")

    def __str__(self):
        return self.plan_type


class Subscription(models.Model):

    client = models.ForeignKey(
        "clients.Client",
        verbose_name=_("client"),
        on_delete=models.PROTECT,
        related_name="subscriptions",
    )
    service = models.ForeignKey(
        "services.Service",
        verbose_name=_("service"),
        on_delete=models.PROTECT,
        related_name="subscriptions",
    )
    plan = models.ForeignKey(
        "services.Plan",
        verbose_name=_("plan"),
        on_delete=models.PROTECT,
        related_name="subscriptions",
    )

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")

    def __str__(self):
        return (
            f"{self.client.user.username}: {self.service.name} - {self.plan.plan_type}"
        )
