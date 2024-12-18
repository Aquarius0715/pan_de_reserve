# Generated by Django 5.1.3 on 2024-12-09 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pan_de_reserve', '0003_alter_bakeryitem_image_alter_bakeryitem_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationdetail',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_name',
            field=models.CharField(max_length=255, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='customer_phone_number',
            field=models.CharField(max_length=20, verbose_name='電話番号'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='receive_time',
            field=models.DateTimeField(verbose_name='受取時間'),
        ),
    ]
