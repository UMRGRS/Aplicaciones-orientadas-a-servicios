from django.db import models
from fernet_fields import EncryptedEmailField, EncryptedCharField

# Create your models here.
class User(models.Model):
    user_name = models.CharField(("Username"), max_length=20, unique=True)
    password = EncryptedCharField(("Password"), max_length=20)
    email = EncryptedEmailField(("Email"), max_length=254)
    signature = models.CharField(("Signature phrase"), max_length=100, default="Hey! write something here")
    
    def __str__(self):
        return(f'ID: {self.pk} Username: {self.user_name}')
    
