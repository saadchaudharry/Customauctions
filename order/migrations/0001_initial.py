# Generated by Django 2.2.7 on 2020-04-25 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_auto_20200424_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_all',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=120)),
                ('address2', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('pincode', models.IntegerField(max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Products')),
            ],
        ),
    ]
