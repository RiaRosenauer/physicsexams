# Generated by Django 3.1.2 on 2020-10-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FSapp', '0004_auto_20201015_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='LatexImages/'),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='subject',
        ),
        migrations.AddField(
            model_name='exercise',
            name='subject',
            field=models.ManyToManyField(blank=True, to='FSapp.Subject'),
        ),
    ]
