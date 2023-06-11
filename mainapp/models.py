from django.db import models
from accounts.models import CustomUser
from django.conf import settings
User = settings.AUTH_USER_MODEL


class CalculationResult(models.Model):
    
    class Meta:
        verbose_name_plural="Koordinatalar"
        
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # name = models.CharField(max_length=20, null=True, blank=True)
    x1 = models.FloatField(default=0, null=True, blank=True)
    x2 = models.FloatField(default=0, null=True, blank=True)
    x3 = models.FloatField(default=0, null=True, blank=True)
    x4 = models.FloatField(default=0, null=True, blank=True)
    y1 = models.FloatField(default=0, null=True, blank=True)
    y2 = models.FloatField(default=0, null=True, blank=True)
    y3 = models.FloatField(default=0, null=True, blank=True)
    y4 = models.FloatField(default=0, null=True, blank=True)
    z1 = models.FloatField(default=0, null=True, blank=True)
    z2 = models.FloatField(default=0, null=True, blank=True)
    z3 = models.FloatField(default=0, null=True, blank=True)
    z4 = models.FloatField(default=0, null=True, blank=True)
    r1 = models.FloatField(default=0, null=True, blank=True)
    r2 = models.FloatField(default=0, null=True, blank=True)
    r3 = models.FloatField(default=0, null=True, blank=True)
    r4 = models.FloatField(default=0, null=True, blank=True)
    rkv1 = models.FloatField(default=0, null=True, blank=True)
    rkv2 = models.FloatField(default=0, null=True, blank=True)
    rkv3 = models.FloatField(default=0, null=True, blank=True)
    rkv4 = models.FloatField(default=0, null=True, blank=True)

    img = models.ImageField(upload_to='img', null=True)
    def __str__(self):
        return f"{self.x1}, {self.y1}, {self.z1}"
    
class ImageClass(models.Model):

    class Meta:
        verbose_name_plural="Rasmlar"

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='graphic_img')
    
    def __str__(self):
        return self.name
    
class WisdomWords(models.Model):
    class Meta:
        verbose_name_plural="Hikmatli so'zlar"
    word = models.TextField()
    author = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.word
