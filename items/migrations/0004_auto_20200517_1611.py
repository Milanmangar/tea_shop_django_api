# Generated by Django 3.0.6 on 2020-05-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20200517_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
