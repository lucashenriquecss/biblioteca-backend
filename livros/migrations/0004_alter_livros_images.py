# Generated by Django 3.2.9 on 2022-01-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_alter_livros_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='images',
            field=models.ImageField(default='', upload_to='', verbose_name='image/'),
        ),
    ]
