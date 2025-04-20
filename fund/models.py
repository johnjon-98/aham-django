from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

class Fund(models.Model):
    id = id = models.BigAutoField(primary_key=True, verbose_name="Fund ID")
    name = models.CharField(max_length=200, verbose_name="Fund Name")
    manager = models.CharField(max_length=100, verbose_name="Fund Manager")
    description = models.CharField(max_length=200, verbose_name="Fund Description")
    net_asset_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fund Net Asset Value (NAV)")
    created_date = models.DateField(auto_now_add=True, verbose_name="Fund Date of Creation")
    performance = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0), validators=PERCENTAGE_VALIDATOR, verbose_name="Fund Performance (as a percentage)")
    
    class Meta:
        ordering = ["id"]
        verbose_name_plural = ["funds"]