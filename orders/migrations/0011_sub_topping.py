# Generated by Django 2.0.3 on 2019-11-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_sub_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub',
            name='topping',
            field=models.ManyToManyField(blank=True, related_name='SubToppings', to='orders.SubTopping'),
        ),
    ]
