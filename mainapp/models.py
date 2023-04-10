from django.db import models
from accounts.models import CustomUser

class CalculationResult(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    x1 = models.IntegerField(default=0, null=True, blank=True)
    x2 = models.IntegerField(default=0, null=True, blank=True)
    x3 = models.IntegerField(default=0, null=True, blank=True)
    y1 = models.IntegerField(default=0, null=True, blank=True)
    y2 = models.IntegerField(default=0, null=True, blank=True)
    y3 = models.IntegerField(default=0, null=True, blank=True)
    z1 = models.IntegerField(default=0, null=True, blank=True)
    z2 = models.IntegerField(default=0, null=True, blank=True)
    z3 = models.IntegerField(default=0, null=True, blank=True)
    r1 = models.IntegerField(default=0, null=True, blank=True)
    r2 = models.IntegerField(default=0, null=True, blank=True)
    r3 = models.IntegerField(default=0, null=True, blank=True)
    img = models.ImageField(upload_to='img', null=True)
    def __unicode__(self):
        return self.name
    
class ImageClass(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='graphic_img')
    
    def __str__(self):
        return self.name