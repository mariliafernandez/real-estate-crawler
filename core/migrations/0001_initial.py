# Generated by Django 4.1.13 on 2023-11-20 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('condo', models.IntegerField()),
                ('area_total', models.IntegerField()),
                ('area_util', models.IntegerField()),
                ('room', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('images_url', models.JSONField()),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.imovel')),
            ],
        ),
    ]