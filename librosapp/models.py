from django.db import models

# Create your models here.
class Libro(models.Model):
    ESTADOS = [
        ("D", "Disponible"),
        ("P", "Prestado"),
        ("R", "Reservado"),
        ("DA", "Dañado"),
        ("PE", "Perdido"),
    ]
    titulo = models.CharField(max_length=100)
    autor=models.CharField(max_length=100)
    editorial=models.CharField(max_length=50)
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default="D"
    )