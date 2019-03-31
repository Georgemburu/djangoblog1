from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 250)
    body = models.TextField()
    image = models.FileField(upload_to='posts_images/%s/')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title