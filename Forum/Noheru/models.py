from django.db import models

from datetime import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(("Username"), max_length=20, unique=True)
    password = models.CharField(("Password"), max_length=20)
    email = models.EmailField(("Email"), max_length=254)
    signature = models.CharField(("Signature phrase"), max_length=100, default="Hey! write something here")
    
    def __str__(self):
        return(f'ID: {self.pk} Username: {self.username}')
    
class Post(models.Model):
    post_title = models.CharField(("Title"), max_length=200)
    post_summary = models.CharField(("Summary"), max_length=100)
    post_content = models.CharField(("Content"), max_length=1000)
    post_publish_date = models.DateTimeField(default=datetime.now())
    up_votes = models.IntegerField(default=0)
    
    #Foreign keys
    creator = models.ForeignKey("User", on_delete=models.CASCADE)
    
    def __str__(self):
        return (f'Post_ID: {self.pk} Post_title: {self.post_title}')

class Comment(models.Model):
    comment_content = models.CharField(("Content"), max_length=500)
    up_votes = models.IntegerField(default=0)
    comment_publish_date = models.DateTimeField(auto_now_add = True)
    
    #Foreign keys
    creator = models.ForeignKey("User", on_delete=models.CASCADE)
    parent_post = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, blank=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='parent')
    
    def __str__(self):
        return (f'ID: {self.pk} Comment: {self.comment_content}')