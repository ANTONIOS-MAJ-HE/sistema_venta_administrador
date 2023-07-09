from django.contrib import admin
from .models import Producto, Rol, Usuario, UsuarioRol, Comentario
# Register your models here.

#visualizacion en /admin
admin.site.register(Producto)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(UsuarioRol)
admin.site.register(Comentario)