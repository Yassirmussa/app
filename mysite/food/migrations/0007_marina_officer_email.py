# Generated by Django 4.1.3 on 2023-01-31 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_marina_officer_confpass_marina_officer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='marina_officer',
            name='email',
            field=models.EmailField(default='yassir@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]