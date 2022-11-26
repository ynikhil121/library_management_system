# Generated by Django 4.1 on 2022-11-26 17:18

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=70)),
                ('Bauthor', models.CharField(max_length=70)),
                ('YearofPub', models.DateField()),
                ('Price', models.FloatField()),
                ('Page', models.IntegerField()),
                ('Category', models.CharField(default='Reference', max_length=40)),
                ('is_deleted', models.CharField(default='n', max_length=2)),
            ],
            managers=[
                ('CustomManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
