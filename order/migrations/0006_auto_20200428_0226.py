# Generated by Django 2.2.7 on 2020-04-27 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20200426_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_all',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100000, null=True),
        ),
    ]