# Generated by Django 5.1.1 on 2024-09-20 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_remove_consulta_id_alter_consulta_id_peticion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='Numero_Documento',
            new_name='Numero_De_Documento',
        ),
    ]
