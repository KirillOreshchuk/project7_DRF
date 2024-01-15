from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Машина')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = "Машины"


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Мотоцикл')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = "Мотоциклы"
