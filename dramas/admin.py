from django.contrib import admin
from .models import Drama


@admin.register(Drama)
class DramaAdmin(admin.ModelAdmin):
    pass
