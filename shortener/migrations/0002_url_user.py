# Generated by Django 3.2.16 on 2022-11-10 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='auth.user'),
            preserve_default=False,
        ),
    ]
