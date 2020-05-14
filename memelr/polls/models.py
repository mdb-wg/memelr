from django.db import models
import django
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=255, default="post title goes here numbnuts")
    post_content = models.ImageField()
    post_date = models.DateTimeField('date posted', default=django.utils.timezone.now())
    postvotes = models.IntegerField(default=0)

class Response(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    respvotes = models.IntegerField(default=0)
    submission_time = models.DateTimeField('date responded', default=django.utils.timezone.now())