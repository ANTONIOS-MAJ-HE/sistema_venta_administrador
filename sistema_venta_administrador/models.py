from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuarios'

class Rol(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'

class UsuarioRol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    rol = models.ForeignKey(Rol, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.usuario} - {self.rol}"

    class Meta:
        db_table = 'usuarios_roles'

class Producto(models.Model):
    cantidad = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'

class Comentario(models.Model):
    cuerpo = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    nombre = models.CharField(max_length=255, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Comentario de {self.nombre}"

    class Meta:
        db_table = 'comentarios'