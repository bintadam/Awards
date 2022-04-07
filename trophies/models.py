from django.db import models

# Create your models here.
class Profile(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)

    class Meta:
        ordering = ['-image']