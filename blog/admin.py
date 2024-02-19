from django.contrib import admin
from .models import *

class ReceptAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at',)
    readonly_fields = ('views',)

admin.site.register(Category)
admin.site.register(Recept, ReceptAdmin)




