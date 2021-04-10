# Create your models here.
from django.db import models

# Create your models here.

class Puesto(models.Model):
    idpuesto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        db_table = "puesto"
        verbose_name = "puesto"

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        db_table = "categoria"
        verbose_name = "categoria"

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono= models.IntegerField()
    condicion_civil= models.CharField(max_length=30)
    puesto_idpuesto= models.ForeignKey(Puesto, on_delete=models.CASCADE, db_column= "idpuesto")
    categoria_idcategoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="idcategoria")

    class Meta:
        db_table = "persona"
        verbose_name = "persona"

class Registro(models.Model):
    idregistro = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    fotoQR= models.ImageField()
    fotorostro = models.ImageField()
    persona_idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column="idpersona")

    class Meta:
        db_table = "registro"
        verbose_name = "registro"



