# Generated by Django 4.2 on 2023-04-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inventory_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Инвентарный номер'),
        ),
        migrations.AlterField(
            model_name='inventorytype',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответственное лицо'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.workers', verbose_name='Сотрудник'),
        ),
    ]
