# Generated by Django 2.2.7 on 2020-04-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('sub_title', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(upload_to='category_img')),
                ('slug', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
