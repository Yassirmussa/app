# Generated by Django 4.1.3 on 2023-01-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_fishermen_marina_officer'),
    ]

    operations = [
        migrations.AddField(
            model_name='marina_officer',
            name='confpass',
            field=models.CharField(default='yassir 23', max_length=200),
        ),
        migrations.AddField(
            model_name='marina_officer',
            name='password',
            field=models.CharField(default='yassir', max_length=200),
            preserve_default=False,
        ),
    ]
