# Generated by Django 3.2.6 on 2021-08-19 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_material_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='front.course'),
        ),
    ]
