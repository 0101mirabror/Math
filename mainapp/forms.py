from django import forms 
from django.contrib.auth.forms import *

class CalculationResultForm(forms.Form):
    x1 = forms.IntegerField(label="x1")
    x2 = forms.IntegerField(label="x2")
    x3 = forms.IntegerField(label="x3")
    x4 = forms.IntegerField(label="x4", required=False)
    y1 = forms.IntegerField(label="y1")
    y2 = forms.IntegerField(label="y2")
    y3 = forms.IntegerField(label="y3")
    y4 = forms.IntegerField(label="y4", required=False)
    z1 = forms.IntegerField(label="z1")
    z2 = forms.IntegerField(label="z2")
    z3 = forms.IntegerField(label="z3")
    z4 = forms.IntegerField(label="z4", required=False)
    r1 = forms.FloatField(label="r1")
    r2 = forms.FloatField(label="r2")
    r3 = forms.FloatField(label="r3")
    r4 = forms.FloatField(label="r4", required=False)
    rkv1 = forms.FloatField(label="R1", required=False)
    rkv2 = forms.FloatField(label="R2", required=False)
    rkv3 = forms.FloatField(label="R3", required=False)
    rkv4 = forms.FloatField(label="R4", required=False)