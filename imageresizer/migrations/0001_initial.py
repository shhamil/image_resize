# Generated by Django 3.2.7 on 2021-09-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pikcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Имя файла')),
                ('file', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, verbose_name='url к картинке для загрузки с указанного url')),
                ('width', models.PositiveIntegerField(default=0, verbose_name='Ширина')),
                ('height', models.PositiveIntegerField(default=0, verbose_name='Высота')),
                ('path_to_image', models.ImageField(blank=True, upload_to='')),
                ('picture', models.CharField(max_length=255)),
                ('parent_picture', models.IntegerField(blank=True, null=True, verbose_name='Исходная картинка')),
            ],
            options={
                'db_table': 'Images',
            },
        ),
    ]