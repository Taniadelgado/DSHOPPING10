# Generated by Django 2.2.6 on 2019-10-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Contries'},
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
