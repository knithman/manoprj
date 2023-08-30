from django.db import models

import uuid


class Kompiuteris(models.Model):
    objects = None
    pavadinimas = models.CharField('Pavadinimas', max_length=80)

    def __str__(self):
        return self.pavadinimas


class Stacionarus(models.Model):
    objects = None
    kompiuteris = models.CharField('Kompiuteris', max_length=100)
    kaina = models.IntegerField('Kaina')
    aprasymas = models.TextField('Aprašymas', max_length=2000)
    kompiuterisFK = models.ForeignKey(Kompiuteris, on_delete=models.SET_NULL, null=True, related_name='stacionarus_set')

    def __str__(self):
        return self.kompiuteris

class Nesiojamas(models.Model):
    objects = None
    kompiuteris = models.CharField('Kompiuteris', max_length=100)
    kaina = models.IntegerField('Kaina')
    aprasymas = models.TextField('Aprašymas', max_length=2000)
    kompiuterisFK = models.ForeignKey(Kompiuteris, on_delete=models.SET_NULL, null=True, related_name='nesiojamas_set')

    def __str__(self):
        return self.kompiuteris
