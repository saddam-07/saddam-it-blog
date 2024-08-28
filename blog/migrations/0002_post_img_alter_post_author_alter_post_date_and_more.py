# Generated by Django 4.2.14 on 2024-08-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='img.jpg', upload_to='image/%Y', verbose_name='Изоброжение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Имя автора'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
