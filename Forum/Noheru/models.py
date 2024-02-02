from django.db import models
from fernet_fields import EncryptedCharField, EncryptedEmailField
# Create your models here.

class Users(models.Model):
    user_name = models.CharField(("Username"), max_length=20, unique=True)
    password = EncryptedCharField(("Password"), max_length=20)
    email = EncryptedEmailField(("Email"), max_length=254, unique=True)
    signature = models.CharField(("Signature phrase"), max_length=100, default="Hey! write something here")
    
class Posts(models.Model):
    post_title = models.CharField(("Title"), max_length=200)
    post_summary = models.CharField(("Summary"), max_length=100)
    post_content = models.CharField(("Content"), max_length=1000)
    post_publish_date = models.DateTimeField(auto_now_add = True)
    up_votes = models.PositiveIntegerField()
    
    #Foreign keys
    user = models.ForeignKey("Users", on_delete=models.CASCADE)

class Responses(models.Model):
    response_content = models.CharField(("Content"), max_length=500)
    up_votes = models.PositiveIntegerField()
    response_publish_date = models.DateTimeField(auto_now_add = True)
    
    #Foreign keys
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    post = models.ForeignKey("Posts", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)