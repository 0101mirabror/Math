from django.db import models

class CalculationResult(models.Model):
    name = models.CharField(max_length=20)
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
    
    def __unicode__(self):
        return self.name