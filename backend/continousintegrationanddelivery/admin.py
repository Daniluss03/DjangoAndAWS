
from django.contrib import admin
# Register your models here.
from .models import Profile

@admin.register(Profile)  # Cambié a usar el decorador
class ProfileAdmin(admin.ModelAdmin):  # Añadí una clase para personalizar el admin
    pass  # Puedes agregar configuraciones personalizadas aquí
