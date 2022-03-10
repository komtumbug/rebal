from django.contrib import admin
from .models import Car, Crypto, Music, Rapper, Games



# Register your models here.


admin.site.register(Rapper)

admin.site.register(Music)

admin.site.register(Car)

admin.site.register(Crypto)

admin.site.register(Games)