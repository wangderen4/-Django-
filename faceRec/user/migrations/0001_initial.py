# Generated by Django 2.1.7 on 2019-05-07 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_h', models.PositiveIntegerField(default=200)),
                ('image_w', models.PositiveIntegerField(default=200)),
                ('img_path', models.ImageField(height_field='image_h', upload_to='user_photo/', width_field='image_w')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=18, unique=True)),
                ('u_icon', models.ImageField(upload_to='user_icon/')),
                ('u_password', models.CharField(max_length=254)),
                ('u_sign', models.TextField()),
                ('u_email', models.EmailField(max_length=254)),
                ('u_ticket', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
