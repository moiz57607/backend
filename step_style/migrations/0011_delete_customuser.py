# Generated by Django 5.0.4 on 2024-05-13 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('step_style', '0010_alter_customuser_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]