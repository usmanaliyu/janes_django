# Generated by Django 2.2.10 on 2020-05-30 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200530_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default='None', max_length=15),
        ),
    ]
