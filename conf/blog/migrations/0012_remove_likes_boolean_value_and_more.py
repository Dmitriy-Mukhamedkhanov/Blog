# Generated by Django 4.2.4 on 2024-02-01 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_likes_boolean_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='boolean_value',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_photo', to=settings.AUTH_USER_MODEL),
        ),
    ]