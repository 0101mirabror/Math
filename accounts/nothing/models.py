from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    class Meta:
        verbose_name_plural="Foydalanuvchilar akkountlari"
    name = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(upload_to="user_img", null=True)
    

