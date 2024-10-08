# Generated by Django 4.2.9 on 2024-03-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='image/', verbose_name='Фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('gift', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Желание',
                'verbose_name_plural': 'Желания',
                'ordering': ['-pub_date'],
            },
        ),
    ]
