from django.db import models

PIECES_CHOICES = (
    ('queen', 'Queen'), ('king', 'King'), ('tower', 'tower'), ('bishop', 'Bishop'), ('pawn', 'Pawn'),
    ('knight', 'Knight')
)
COLOR_CHOICES = (('white', 'White'), ('black', 'Black'))


# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=5, choices=COLOR_CHOICES)

    def __str__(self):
        return self.name


class Piece(models.Model):
    name = models.CharField(max_length=6, choices=PIECES_CHOICES)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return f'{self.name} - {self.color.name}'

    class Meta:
        ordering = ['name']
