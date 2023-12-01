# Generated by Django 4.1.3 on 2022-12-10 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_service',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_pieces',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_services',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='reservation',
            name='total_price',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.IntegerField(default=0, max_length=30),
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=30)),
                ('price', models.IntegerField(default='', max_length=30)),
                ('workforce_price', models.IntegerField(default=0, max_length=30)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
