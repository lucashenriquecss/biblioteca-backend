# Generated by Django 3.2.9 on 2022-01-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_auto_20220101_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='images',
            field=models.ImageField(default='', upload_to='', verbose_name='media/%d/%m/%Y'),
        ),
    ]
