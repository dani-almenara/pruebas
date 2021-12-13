from django.contrib import admin
from .models import CountryCodes, TypeEvent, Event


admin.site.register(Event)
admin.site.register(CountryCodes)
admin.site.register(TypeEvent)