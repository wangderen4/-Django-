# Generated by Django 2.1.7 on 2019-05-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='u',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='img_path',
            field=models.ImageField(height_field=models.PositiveIntegerField(default=200), upload_to='user_photo/', width_field=models.PositiveIntegerField(default=200)),
        ),
    ]