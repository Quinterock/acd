# Generated by Django 3.2.5 on 2021-07-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='arte',
            name='descripcion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
