from django.db import models
from fernet_fields import EncryptedCharField, EncryptedEmailField
# Create your models here.

class Users(models.Model):
    user_name = models.CharField(("Username"), max_length=20, unique=True)
    password = EncryptedCharField(("Password"), max_length=20)
    email = EncryptedEmailField(("Email"), max_length=254)
    signature = models.CharField(("Signature phrase"), max_length=100, default="Hey! write something here")
    
    def __str__(self):
        return(f'ID: {self.pk} Username: {self.user_name}')
    
class Posts(models.Model):
    post_title = models.CharField(("Title"), max_length=200)
    post_summary = models.CharField(("Summary"), max_length=100)
    post_content = models.CharField(("Content"), max_length=1000)
    post_publish_date = models.DateTimeField()
    up_votes = models.IntegerField(default=0)
    
    #Foreign keys
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    
    def __str__(self):
        return (f'Post_ID: {self.pk} Post_title: {self.post_title}')

class Responses(models.Model):
    response_content = models.CharField(("Content"), max_length=500)
    up_votes = models.IntegerField(default=0)
    response_publish_date = models.DateTimeField(auto_now_add = True)
    
    #Foreign keys
    user = models.ForeignKey("Users", on_delete=models.CASCADE)
    post = models.ForeignKey("Posts", on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return (f'ID: {self.pk} Response: {self.response_content}')