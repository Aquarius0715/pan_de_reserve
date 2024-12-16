# Generated by Django 5.1.3 on 2024-12-12 16:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pan_de_reserve', '0005_alter_reservation_is_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservationdetail',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservationdetail',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='個数'),
        ),
    ]