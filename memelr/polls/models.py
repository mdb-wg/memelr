from django.db import models

# Create your models here.
class Post(models.Model):
    post_content = models.ImageField()
    post_date = models.DateTimeField('date posted')
    postvotes = models.IntegerField(default=0)

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    respvotes = models.IntegerField(default=0)
    submission_time = models.DateTimeField('date responded')