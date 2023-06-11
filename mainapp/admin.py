from django.contrib import admin

"Local"
from .models import CalculationResult
from .models import ImageClass, WisdomWords

admin.site.register(CalculationResult)
admin.site.register(ImageClass)
admin.site.register(WisdomWords)
