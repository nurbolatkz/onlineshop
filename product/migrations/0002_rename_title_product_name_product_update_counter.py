# Generated by Django 4.0.4 on 2022-11-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='update_counter',
            field=models.IntegerField(default=0),
        ),
    ]
