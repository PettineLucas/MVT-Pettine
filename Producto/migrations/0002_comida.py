# Generated by Django 4.1 on 2022-08-26 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_created=True, auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]