# Generated by Django 3.2.6 on 2021-08-19 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_notification_date_added'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Update',
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name_plural': 'Semester'},
        ),
    ]
