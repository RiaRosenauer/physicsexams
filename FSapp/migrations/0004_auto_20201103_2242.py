# Generated by Django 3.1.2 on 2020-11-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0003_auto_20201103_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='answer',
            new_name='answer1',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question',
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer10',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer2',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer3',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer4',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer5',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer6',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer7',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer8',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='answer9',
            field=models.ImageField(blank=True, null=True, upload_to='solution'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question1',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question10',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question2',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question3',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question4',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question5',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question6',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question7',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question8',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='question9',
            field=models.ImageField(blank=True, null=True, upload_to='question'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]