# Generated by Django 2.2.6 on 2019-11-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_sub_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtopping',
            name='price_l',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='subtopping',
            name='price_s',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
