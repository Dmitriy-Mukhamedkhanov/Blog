# Generated by Django 4.2.4 on 2023-08-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_like_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_comment',
            field=models.TextField(max_length=20, verbose_name='Имя'),
        ),
    ]