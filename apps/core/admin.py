from apps.core.models import Documento
from django.contrib import admin

# Register your models here.
@admin.register(Documento)
class PassagemAdmin(admin.ModelAdmin):
    search_fields = [ "documento", "tipo"]
    list_display = ["documento", "tipo", "criado",]
    list_filter = ["tipo"]
    readonly_fields = ["criado", "modificado" ]