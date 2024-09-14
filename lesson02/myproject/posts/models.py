from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    ## migrations are nessary only if the model is changed not id methods are added 
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField() #slug is what shows up at the end of the url
    date = models.DateTimeField(auto_now_add=True) # date time stamp auto added to post 
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title