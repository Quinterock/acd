# Generated by Django 3.2.5 on 2021-07-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Deportes', '0002_rename_deportek_deportes'),
    ]

    operations = [
        migrations.AddField(
            model_name='deportes',
            name='descripcion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
