# Generated by Django 4.1.3 on 2023-01-31 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=200)),
                ('img', models.FileField(upload_to='pictures')),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]