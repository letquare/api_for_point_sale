from django.db import models


class Employee(models.Model):

    first_name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=30)

    def __str__(self):
        return f'{self.first_name}'


class PointOfSale(models.Model):

    title = models.CharField('Название', max_length=255)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        related_name='employee',
        blank=False,
        null=True
    )

    def __str__(self):
        return f'{self.title}'


class Visit(models.Model):

    datatime = models.DateTimeField('Дата и время', auto_now=True)
    point_sale = models.ForeignKey(
        PointOfSale,
        on_delete=models.CASCADE,
        related_name='point_sail',
        blank=False,
    )
    visitor = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='visitor',
        blank=False,
        null=True
    )
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.pk}, {self.point_sale}, {self.visitor}'
