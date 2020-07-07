# Generated by Django 2.2 on 2020-07-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200623_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transistors',
            name='division',
            field=models.CharField(blank=True, choices=[('general', 'General'), ('bjt_npn', 'BJT_NPN'), ('bjt_pnp', 'BJT_PNP')], max_length=15),
        ),
    ]
