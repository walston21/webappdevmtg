from django.contrib import admin

# Register your models here.
from mtg_app.models import MTGCard

class MTGCardAdmin(admin.ModelAdmin):
    fields = ('name', 'colors')

admin.site.register(MTGCard, MTGCardAdmin)
