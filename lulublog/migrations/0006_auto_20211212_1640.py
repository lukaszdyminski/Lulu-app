# Generated by Django 3.2.9 on 2021-12-12 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lulublog', '0005_auto_20211212_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lulupostcomment',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor komentarza'),
        ),
        migrations.AlterField(
            model_name='petpostcomment',
            name='name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor komentarza'),
        ),
    ]
