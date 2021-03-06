# Generated by Django 3.2.9 on 2021-12-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lulublog', '0010_auto_20211215_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lulupostcomment',
            name='rate',
            field=models.CharField(choices=[('1 * Lulu rozczarowana', '1 * LULU ROZCZAROWANA'), ('2 ** Lulu marudna', '2 ** LULU MARUDNA'), ('3 *** Lulu zainteresowana', '3 *** LULU ZAINTERESOWANA'), ('4 **** Lulu pobudzona', '4 **** LULU POBUDZONA'), ('5 ***** Lulu podekscytowana', '5 ***** LULU PODEKSCYTOWANA')], default=None, max_length=30, verbose_name='Ocena'),
        ),
        migrations.AlterField(
            model_name='petpostcomment',
            name='rate',
            field=models.CharField(choices=[('1 * Lulu rozczarowana', '1 * LULU_ROZCZAROWANA'), ('2 ** Lulu marudna', '2 ** LULU_MARUDNA'), ('3 *** Lulu zainteresowana', '3 *** LULU_ZAINTERESOWANA'), ('4 **** Lulu pobudzona', '4 **** LULU_POBUDZONA'), ('5 ***** Lulu podekscytowana', '5 ***** LULU_PODEKSCYTOWANA')], default=None, max_length=30, verbose_name='Ocena'),
        ),
    ]
