from django.contrib import admin

"Local"
from .models import CalculationResult
from .models import ImageClass

admin.site.register(CalculationResult)
admin.site.register(ImageClass)
