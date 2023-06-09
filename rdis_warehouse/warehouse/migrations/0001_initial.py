# Generated by Django 4.2 on 2023-04-18 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id_inventory', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_name', models.CharField(max_length=50, verbose_name='Название')),
                ('inventory_number', models.CharField(max_length=50, verbose_name='Инвентарный номер')),
                ('specifications', models.TextField(blank=True, null=True, verbose_name='Характеристики')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус активности')),
            ],
            options={
                'verbose_name': 'Инвентарь',
                'verbose_name_plural': 'Инвентарь',
            },
        ),
        migrations.CreateModel(
            name='StorageLocation',
            fields=[
                ('id_location', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=20, verbose_name='Название расположения')),
            ],
            options={
                'verbose_name': 'Расположение хранилища',
                'verbose_name_plural': 'Расположения хранилищ',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id_worker', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('first_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id_storage', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.inventory', verbose_name='Инвентарь')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.storagelocation', verbose_name='Место нахождения')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.workers', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Учет',
                'verbose_name_plural': 'Учеты',
            },
        ),
        migrations.CreateModel(
            name='InventoryType',
            fields=[
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50, verbose_name='Название типа инвентаря')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответсвенное лицо')),
            ],
            options={
                'verbose_name': 'Тип Инвентаря',
                'verbose_name_plural': 'Тип Инвентаря',
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.inventorytype', verbose_name='Тип инвентаря'),
        ),
    ]
