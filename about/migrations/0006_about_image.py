# Generated by Django 4.0.4 on 2022-06-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_about_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(default='avatar.jpg', null=True, upload_to=''),
        ),
    ]
