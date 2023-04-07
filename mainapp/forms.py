from django import forms 
from django.contrib.auth.forms import *

class CalculationResultForm(forms.Form):
    x1 = forms.IntegerField(label="x1")
    x2 = forms.IntegerField(label="x2")
    x3 = forms.IntegerField(label="x3")
    y1 = forms.IntegerField(label="y1")
    y2 = forms.IntegerField(label="y2")
    y3 = forms.IntegerField(label="y3")
    z1 = forms.IntegerField(label="z1")
    z2 = forms.IntegerField(label="z2")
    z3 = forms.IntegerField(label="z3")
    r1 = forms.IntegerField(label="r1")
    r2 = forms.IntegerField(label="r2")
    r3 = forms.IntegerField(label="r3")