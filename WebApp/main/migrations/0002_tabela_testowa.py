# Generated by Django 3.1.2 on 2020-10-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabela_testowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('temperature', models.IntegerField()),
                ('param', models.IntegerField()),
            ],
        ),
    ]