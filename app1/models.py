from django.db import models
from datetime import date, datetime

# Create your models here.
class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        print(postData['titulo'])
        if len(postData['titulo'])<2:
            errors['titulo'] = "El largo del titulo debe ser mayor a 1"
        if len(postData['cadena'])<3:
            errors['cadena'] = "El largo del nombre de la cadena de televisión debe ser mayor a 1"
        if len(postData['descripcion'])>0 and len(postData['descripcion'])<11:
            errors['descripcion'] = "La descripción puede estar vacía o debe contener al menos 10 caracteres"
        if  postData['fecha_lanz'] > str(date.today()):
            errors['fecha_lanz'] = "La fecha debe estar en el pasado"
        if len(postData['fecha_lanz']) != 10:
            errors['fecha_lanz'] = "Ingrese correctamente la fecha"

        if postData['nuevo'] == "True":
            for s in Show.objects.all():
                # se usa .lower() para ovbiar las mayúsculas en la comparación de palabras
                if postData['titulo'].lower() == s.title.lower(): 
                    errors['titulo'] = "Este titulo ya existe"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



