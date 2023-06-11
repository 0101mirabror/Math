from django.db import models
# from django.contrib.auth.models import User
from PIL import Image

from django.conf import settings
User = settings.AUTH_USER_MODEL
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    class Meta:
        verbose_name_plural="Foydalanuvchilar akkountlari"
    name = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(upload_to="user_img", null=True)
    
