# Generated by Django 3.0.4 on 2020-03-21 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('url', models.URLField(unique=True)),
                ('topic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='testing.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AccesssRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='testing.Webpage')),
            ],
        ),
    ]
