# Generated by Django 4.2.4 on 2024-02-01 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_likes_boolean_value_likes_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='user_id',
            new_name='user',
        ),
    ]
