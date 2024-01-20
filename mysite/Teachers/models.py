from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class ContractType(models.Model):
    class FullOrPart(models.TextChoices):
        FULL = "FT", _("Full time")
        PART = "PT", _("Part time")
        
    contract = models.CharField(('Tipo de contrato'), max_length=2, choices=FullOrPart)
    
    def __str__(self):
        return self.contract

   
class TeachersInfo(models.Model):
    
    class MaleOrFemale(models.TextChoices):
        MALE = "M", _("Masculino")
        FEMALE = "F", _("Femenino")
    
    name = models.CharField(("Nombre/s"), max_length=100)
    lastname1 = models.CharField(("Apellido 1"), max_length=100)
    lastname2 = models.CharField(("Apellido 1"), max_length=100)
    age = models.PositiveIntegerField(("Edad"))
    maloOrFemale = models.CharField(('Sexo'), max_length=1, choices=MaleOrFemale)
    contractType = models.ForeignKey(ContractType, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'Nombre: {self.name} Apellido 1: {self.lastname1} Apellido 2: {self.lastname2}'
        
    