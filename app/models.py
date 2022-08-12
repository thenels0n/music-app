from django.db import models

# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to='media/', null=True)
    song = models.FileField(upload_to='media')
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
