# Generated by Django 3.1.2 on 2020-11-03 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0005_auto_20201103_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='answer1',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='question1',
            new_name='question',
        ),
    ]