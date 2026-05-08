from django.db import models

# Create your models here.
class ContractUs(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    problem = models.TextField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "contract us"
    