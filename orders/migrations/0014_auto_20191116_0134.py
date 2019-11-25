# Generated by Django 2.2.6 on 2019-11-15 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_cartitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='orderID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Order'),
        ),
    ]