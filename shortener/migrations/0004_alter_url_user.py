# Generated by Django 3.2.16 on 2022-11-11 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0003_alter_url_url_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='url', to=settings.AUTH_USER_MODEL),
        ),
    ]
