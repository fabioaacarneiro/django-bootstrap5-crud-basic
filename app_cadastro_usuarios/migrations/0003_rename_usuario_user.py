# Generated by Django 4.2.5 on 2023-09-05 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
    ]
