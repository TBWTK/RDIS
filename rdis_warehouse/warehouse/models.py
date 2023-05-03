from django.db import models
from django.contrib.auth.models import User


class StorageLocation(models.Model):
    id_location = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=20, verbose_name='Название расположения')

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = "Расположения хранилищ"
        verbose_name = "Расположение хранилища"


class Workers(models.Model):
    id_worker = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='Имя')
    first_name = models.CharField(max_length=20, verbose_name='Фамилия')
    last_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='Отчество')

    def __str__(self):
        return f"{self.first_name} {self.name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"


class InventoryType(models.Model):
    id_type = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, verbose_name='Название типа инвентаря')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ответственное лицо')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = "Тип Инвентаря"
        verbose_name = "Тип Инвентаря"


class Inventory(models.Model):
    id_inventory = models.AutoField(primary_key=True)
    type = models.ForeignKey(InventoryType, on_delete=models.CASCADE, verbose_name='Тип инвентаря')
    inventory_name = models.CharField(max_length=50, verbose_name='Название')
    inventory_number = models.CharField(max_length=50, verbose_name='Инвентарный номер', null=True, blank=True)
    specifications = models.TextField(verbose_name='Характеристики', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    def __str__(self):
        return f"{self.type} {self.inventory_name} | Номер:{self.inventory_number}"

    class Meta:
        verbose_name_plural = "Инвентарь"
        verbose_name = "Инвентарь"


class Storage(models.Model):
    id_storage = models.AutoField(primary_key=True)
    location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE, verbose_name='Место нахождения')
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, verbose_name='Инвентарь')
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='Сотрудник', null=True, blank=True)

    start_date = models.DateField(null=True, verbose_name='Дата начала')
    end_date = models.DateField(null=True, verbose_name='Дата окончания', )
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    def __str__(self):
        return f"{self.location} {self.inventory} {self.worker}"

    class Meta:
        verbose_name_plural = "Учеты"
        verbose_name = "Учет"
