from django.contrib import admin
from .models import Photos 
from .models import Users 

# імпорт твоєї моделі


admin.site.register(Photos)
admin.site.register(Users)

