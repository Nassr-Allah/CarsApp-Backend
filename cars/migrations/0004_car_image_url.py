# Generated by Django 4.1.3 on 2022-12-05 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_url',
            field=models.CharField(default='', max_length=300),
        ),
    ]
