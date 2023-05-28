# Generated by Django 4.2.1 on 2023-05-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.CharField(default='/media/default.jpg', max_length=100, null=True, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Аватар'),
        ),
    ]