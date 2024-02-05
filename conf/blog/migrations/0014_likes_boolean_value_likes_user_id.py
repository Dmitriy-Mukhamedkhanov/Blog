# Generated by Django 4.2.4 on 2024-02-01 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_author_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='boolean_value',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='likes',
            name='user_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
